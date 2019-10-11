from flask import jsonify, request, g
from flask import g, abort

from webapp.api.auth import token_auth

from webapp import db
from webapp.api import bp
from webapp.api.errors import bad_request
from webapp.main.models import Compte, Operation


@bp.route('/comptes/<int:id>/operations', methods=['GET'])
@token_auth.login_required
def get_operations(id):
    """Renvoie toutes les opérations d'un compte de la personne authentifiée
        test httpie:
        http GET http://localhost:5000/api/comptes/2/operations "Authorization:Bearer sCzzknjzsA/VVGstIcvYz7CmJKpFwJ9u"
    """
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 10, type=int), 100)
    compte = Compte.query.get_or_404(id)
    if g.current_user.id != compte.titulaire_id:
        return bad_request('Veuillez utiliser un identifiant de compte différent')
    operations = Operation.to_collection_dict(compte.operations.union_all(compte.virements),
                                              page,
                                              per_page,
                                              'api.get_operations',
                                              id=id)
    return jsonify(operations)


