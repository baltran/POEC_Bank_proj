from flask import jsonify, request, g
from flask import g, abort

from webapp.api.auth import token_auth

from webapp import db
from webapp.api import bp
from webapp.api.errors import bad_request, conflict_request, denied_request
from webapp.main.models import Compte, Operation


@bp.route('/comptes/<int:id>/operations', methods=['GET'])
@token_auth.login_required
def get_operations(id):
    """Renvoie toutes les opérations d'un compte de la personne authentifiée
        test httpie:
        http GET http://localhost:5000/api/comptes/<int:id>/operations "Authorization:Bearer sCzzknjzsA/VVGstIcvYz7CmJKpFwJ9u"
    """
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 10, type=int), 100)
    compte = Compte.query.get_or_404(id)
    if g.current_user.id != compte.titulaire_id:
        return denied_request('Veuillez utiliser un identifiant de compte différent')
    operations = Operation.to_collection_dict(compte.operations.union_all(compte.virements).order_by(Operation.done_at.desc()),
                                              page,
                                              per_page,
                                              'api.get_operations',
                                              id=id)
    operations.update({'solde': compte.solde})
    return jsonify(operations)


@bp.route('/comptes/<int:id>/depot', methods=['PUT'])
@token_auth.login_required
def set_deposit(id):
    """ Permet le depot sur un compte de la personne authentifiée
        test httpie:
        http PUT http://localhost:5000/api/comptes/<int:id>/depot "Authorization:Bearer sCzzknjzsA/VVGstIcvYz7CmJKpFwJ9u"
    """
    compte = Compte.query.get_or_404(id)
    data = request.get_json() or {}
    if g.current_user.id != compte.titulaire_id:
        return denied_request('Veuillez utiliser un identifiant de compte différent')
    if 'valeur' in data and not data['valeur']:
        return bad_request('Veuillez mettre un nombre')
    if 'valeur' not in data:
        return bad_request('Veuillez ajouter une valeur')
    try:
        increment = int(data['valeur'])
    except (ValueError, TypeError):
        bad_request('Veuillez mettre un nombre')
    else:
        increment = abs(increment)
        compte.solde += increment
        data_depot = {'valeur': increment, 'compte_id': compte.id, 'type_operation': 'depot'}
        operation = Operation(**data_depot)
        db.session.add(operation)
        db.session.commit()
        return jsonify(operation.to_dict())


@bp.route('/comptes/<int:id>/retrait', methods=['PUT'])
@token_auth.login_required
def set_withdrawal(id):
    """ Permet le retrait sur un compte de la personne authentifiée
        test httpie:
        http PUT http://localhost:5000/api/comptes/<int:id>/retrait "Authorization:Bearer sCzzknjzsA/VVGstIcvYz7CmJKpFwJ9u"
    """
    compte = Compte.query.get_or_404(id)
    data = request.get_json() or {}
    if g.current_user.id != compte.titulaire_id:
        return denied_request('Veuillez utiliser un identifiant de compte différent')
    if 'valeur' in data and not data['valeur']:
        return bad_request('Veuillez mettre un nombre')
    if 'valeur' not in data:
        return bad_request('Veuillez ajouter une valeur')
    try:
        decrement = int(data['valeur'])
    except (ValueError, TypeError):
        return bad_request('Veuillez mettre un nombre')
    else:
        decrement = abs(decrement)
        solde_tmp = compte.solde - decrement
        if solde_tmp < 0:
            if not compte.autorisation_decouvert:
                return conflict_request("Le compte n'a pas d'autorisation de découvert")
            elif solde_tmp < (0 - (compte.entree_moyenne * compte.taux_decouvert)):
                return conflict_request("L'operation demandée dépasse le seuil de découvert")
        data = (solde_tmp, compte.rib)
        compte.solde = solde_tmp
        data_retrait = {'valeur': -decrement, 'compte_id': compte.id, 'type_operation': 'retrait'}
        operation = Operation(**data_retrait)
        db.session.add(operation)
        db.session.commit()
        return jsonify(operation.to_dict())


