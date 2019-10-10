from flask import render_template, request
from webapp.conseiller import bp
from webapp.main.classes.demande import Demande
from webapp.main.classes.client import Client
from webapp.main.classes.utilisateur import db


# from webapp.main.classes.conseiller import Conseiller


@bp.route('/gerer_demande', methods=['GET', 'POST'])
def gerer_demandes():
    my_string = request.full_path
    id = -1
    clients = Client.query.all()
    demandes = Demande.query.all()
    # data={}
    if 'accepter' in my_string:
        id = int(my_string.split("=", 1)[1])
        data = Demande.query.filter_by(id=id)[0].afficher()
        del data['id']
        client = Client(**data)
        demande = Demande.query.filter_by(id=id)[0]
        db.session.add(client)
        db.session.delete(demande)
        db.session.commit()
        clients = Client.query.all()
        demandes = Demande.query.all()

    elif 'refuser' in my_string:
        # Efface l'entrée dans la table Demande
        id = int(my_string.split("=", 1)[1])
        demande = Demande.query.filter_by(id=id)[0]
        db.session.delete(demande)
        db.session.commit()
        demandes = Demande.query.all()

    elif 'supprimer' in my_string:
        id = int(my_string.split("=", 1)[1])
        client = Client.query.filter_by(id=id)[0]
        db.session.delete(client)
        db.session.commit()
        clients = Client.query.all()

    return render_template('conseiller/gerer_demandes.html',
                       title="Gestion des demandes",
                       clients=clients,
                       demandes=demandes)
