from flask import render_template
from webapp.conseiller import bp
from webapp.main.classes.demande import Demande
from webapp.main.requetes import select_all
# from webapp.main.classes.conseiller import Conseiller



@bp.route('/index')
@bp.route('/gerer_demandes')
# @login_required
def gerer_demandes():
    # requests = select_all(Demande)
    requests = Demande.query.all()
    # conseillers = select_all(Conseiller)
    return render_template('conseiller/gerer_demandes.html',
                           title="Gestion des demandes",
                           requests=requests)
