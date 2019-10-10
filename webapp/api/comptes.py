from flask import jsonify, request
from flask import g, abort
from flask_login import current_user

from webapp.api.auth import token_auth

from webapp import db
from webapp.api import bp
from webapp.api.errors import bad_request
from webapp.main.models import Compte, Operation


@bp.route('/comptes/<int:id>/operations', methods=['GET'])
@token_auth.login_required
#@bp.endpoint('api.get_operations')
def get_operations(id):
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 10, type=int), 100)
    compte = Compte.query.get_or_404(id)
    if current_user.id != compte.titulaire_id:
        return bad_request('Veuillez utiliser un identifiant de compte différent')
    operations = Operation.to_collection_dict(compte.operations, page, per_page, 'api.get_operations', id=id)
    virements_recus = Operation.to_collection_dict(compte.virements, page, per_page, 'api.get_operations', id=id)
    return jsonify(Operation.to_collection_dict(compte.operations, page, per_page, 'api.get_operations'))


