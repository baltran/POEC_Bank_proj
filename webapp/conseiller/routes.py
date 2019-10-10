from flask import render_template, request
from webapp.conseiller import bp
from webapp.main.classes.demande import Demande
from webapp.conseiller.forms import AcceptForm
from webapp.main.classes.client import Client
from webapp.main.classes.utilisateur import db
# from webapp.main.classes.conseiller import Conseiller



@bp.route('/index')
@bp.route('/gerer_demandes', methods=['GET', 'POST'])
# @login_required
def gerer_demandes():
    demandes = Demande.query.all()
    users = Client.query.all()
    # conseillers = select_all(Conseiller)
    return render_template('conseiller/gerer_demandes.html',
                           title="Gestion des demandes",
                           users=users,
                           demandes=demandes)

@bp.route('/accepter_demande', methods=['GET', 'POST'])
def accepter_demande():
    form=AcceptForm()
    if 'accept' in request.data:
        if 'accepter' in form.action:
            print(form.action)
            data = Demande.query.filter_by(id=id)[0].afficher()
            client = Client(**data)
            db.session.add(client)
            db.session.commit()
            # Effacer l'entrée dans la table Demande
            # pass  # do something
        elif 'refuser' in form.action:
            # Effacer l'entrée dans la table Demande
            pass  # do something else
    users = Client.query.all()
    demandes = Demande.query.all()
    return render_template('conseiller/redirect.html',
                           title="Gestion des demandes",
                           users=users,
                           demandes=demandes)
