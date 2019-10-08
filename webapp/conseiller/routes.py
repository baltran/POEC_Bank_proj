from flask import render_template
from webapp.auth import bp
from webapp.main.classes.demande import Demande


@bp.route('/conseiller/gerer_demandes')
# @login_required
def index():
    requests = select_all(Demande)
    return render_template('main/index.html',
                           title="Gestion des demandes",
                           requests=requests))
