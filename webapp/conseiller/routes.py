from flask import render_template, request
from webapp.conseiller import bp
from webapp.main.classes.demande import Demande
from webapp.main.classes.client import Client
from webapp.main.classes.utilisateur import db


# from webapp.main.classes.conseiller import Conseiller


@bp.route('/gerer_demande', methods=['GET', 'POST'])
#@login_required
# TODO: Assurer que seulement les conseillers peuvent y accéder.
def gerer_demandes():
    my_string = request.full_path
    ids_demandes = Demande.query.with_entities(Demande.id).all()
    ids_clients = Client.query.with_entities(Client.id).all()
    print("Il y a ",len(ids_demandes),"demandes")

    # Pour ne pas crasher en absence de clients:
    c=Client(id=1, username='', email='', discriminator='client')
    client_null = [c]
    # Pour ne pas crasher en absence de demandes:
    d=Demande(id=1, username='', email='')
    demande_null=[c]

    clients = Client.query.all()
    demandes = Demande.query.all()

    if 'accepter' in my_string:
        id = int(my_string.split("=", 1)[1])
        if (id,) in ids_demandes:
            print(ids_demandes)
            data = Demande.query.get(id).afficher()
            del data['id']
            client = Client(**data)
            demande = Demande.query.get(id)
            db.session.add(client)
            db.session.delete(demande)
            db.session.commit()
            clients = Client.query.all()
            demandes = Demande.query.all()
        else:
            pass

    elif 'refuser' in my_string:
        id = int(my_string.split("=", 1)[1])
        # Efface l'entrée dans la table Demande
        if (id,) in ids_demandes:
            demande = Demande.query.get(id)
            db.session.delete(demande)
            db.session.commit()
            demandes = Demande.query.all()

    elif 'supprimer' in my_string:
        id = int(my_string.split("=", 1)[1])
        if (id,) in ids_clients:
            id = int(my_string.split("=", 1)[1])
            client = Client.query.get(id)
            db.session.delete(client)
            db.session.commit()
            clients = Client.query.all()

    # if clients == []:
    #     clients = client_null
    # if demandes == []:
    #     demande = demande_null
    #
    total_de_clients = Client.query.count()
    total_de_demandes = Demande.query.count()
    #
    return render_template('conseiller/gerer_demandes.html',
                        title="Gestion des demandes",
                        clients=clients,
                        demandes=demandes,
                        total_de_demandes=total_de_demandes,
                        total_de_clients=total_de_clients,
                        ids_demandes=ids_demandes)