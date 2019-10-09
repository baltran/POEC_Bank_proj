from flask import render_template
from webapp.conseiller import bp
from webapp.main.classes.demande import Demande
# from webapp.main.classes.conseiller import Conseiller


@bp.route('/conseiller/gerer_demandes')
# @login_required
def index():
    requests = select_all(Demande)
    # conseillers = select_all(Conseiller)
    return render_template('conseiller/gerer_demandes.html',
                           title="Gestion des demandes",
                           requests=requests)
