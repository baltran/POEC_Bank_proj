from flask import render_template, request, send_file, redirect, url_for
from flask_login import current_user, login_required

from webapp.conseiller import bp
from webapp.main.classes.demande import Demande
from webapp.main.classes.client import Client
# from webapp.main.classes.compte import CompteCourant
from webapp.main.classes.utilisateur import db
from io import BytesIO
from werkzeug.security import generate_password_hash
import numpy as np
from webapp.auth.email import send_password_new_account_email
import time
from flask_babel import _, lazy_gettext as _l


# from webapp.main.classes.conseiller import Conseiller


@bp.route('/index', methods=['GET'])
@bp.route('/gerer_demandes', methods=['GET', 'POST'])
@bp.endpoint('gerer_demandes')
@login_required
# TODO: Assurer que seulement les conseillers peuvent y accéder. (Victor : fait)
def gerer_demandes():
    if current_user.is_authenticated and current_user.discriminator == 'conseiller':
        my_string = request.full_path
        ids_demandes = Demande.query.with_entities(Demande.id).all()
        ids_clients = Client.query.with_entities(Client.id).all()
        print("Il y a ", len(ids_demandes), "demandes")

        clients = Client.query.all()
        demandes = Demande.query.all()

    if 'accepter' in my_string:
        id = int(my_string.split("=", 1)[1])
        if (id,) in ids_demandes:
            print(ids_demandes)
            data = Demande.query.get(id).data_dict()
            del data['id']
            # CREATE A CLIENT
            client = Client(**data)
            demande = Demande.query.get(id)
            # generate a random password
            # first choose a seed
            np.random.seed(int(time.time()))
            # then a random int from 1 to 100 included
            random_int = np.random.randint(1, 101)
            # Use the seed to choose a random length for the password between 12 and 15 characters
            random_length = np.random.randint(12, 16)
            # Now the password correspond to the last random_lenght carachters of the random_int hash:
            random_pass = generate_password_hash(str(random_int))[-random_length:]
            # Add the password to the client object
            client.password = generate_password_hash(random_pass)
            # Save the object in the database
            db.session.add(client)
            db.session.delete(demande)
            # db.session.commit()
            # client_id = Client.query.filter_by(username=data['username']).first().id
            # # CREATE NEW ACCOUNT
            # new_account = CompteCourant(titulaire_id=client_id)
            # new_account.discriminator = 'compte_courant'
            # db.session.add(new_account)
            db.session.commit()
            send_password_new_account_email(client, random_pass)
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

    total_de_clients = Client.query.count()
    total_de_demandes = Demande.query.count()

    return render_template('conseiller/gerer_demandes.html',
                           title="Gestion des demandes",
                           clients=clients,
                           demandes=demandes,
                           total_de_demandes=total_de_demandes,
                           total_de_clients=total_de_clients,
                           ids_demandes=ids_demandes)


@bp.route('/display_piece_id', methods=['GET', 'POST'])
@bp.endpoint('display_piece_id')
def display_piece_id():
    my_string = request.full_path
    if "=" in my_string:
        id = int(my_string.split("=", 1)[1])
        demande_data = Demande.query.get(id).piece_id
        # Returning Files From a Database in Flask
        # https: // www.youtube.com / watch?v = QPI3rzZow6k
        return send_file(BytesIO(demande_data), attachment_filename="flask.pdf", as_attachment=True)
    else:
        return render_template('conseiller/display_piece_id.html')


@bp.route('/display_just_domicile')
@bp.endpoint('display_just_domicile')
def display_just_domicile():
    my_string = request.full_path
    if "=" in my_string:
        id = int(my_string.split("=", 1)[1])
        demande_data = Demande.query.get(id).just_domicile
        # Returning Files From a Database in Flask
        # https: // www.youtube.com / watch?v = QPI3rzZow6k
        return send_file(BytesIO(demande_data), attachment_filename="flask.pdf", as_attachment=True)
    else:
        return render_template('conseiller/display_just_domicile.html')


@bp.route('/display_just_salaire')
@bp.endpoint('display_just_salaire')
def display_just_salaire():
    my_string = request.full_path
    if "=" in my_string:
        id = int(my_string.split("=", 1)[1])
        demande_data = Demande.query.get(id).just_salaire
        # Returning Files From a Database in Flask
        # https: // www.youtube.com / watch?v = QPI3rzZow6k
        return send_file(BytesIO(demande_data), attachment_filename="flask.pdf", as_attachment=True)
    else:
        return render_template('conseiller/display_just_salaire.html')
