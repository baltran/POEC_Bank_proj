from webapp import db
from webapp.main.models import *
from werkzeug.security import generate_password_hash as gph
from webapp.main.requetes import inserer, delete_database_data

data_cli = {'username': 'Baltran', 'password': gph('elpoto'), 'email': 'daubie_vic@msn.com',
            'adresse': '10, rue de la liberté', 'telephone': '0123456789'}
data_admin = {'username': 'admin', 'password': gph('admin'), 'email': 'admin@gestibank.fr'}

data_conseiller = {'username': 'Bob', 'password': gph('bob'), 'email': 'bob@bip.fr'}
data_demande = {'username': 'Bernard', 'password': gph('bernard'), 'email': 'bern@bip.fr', 'tel': '0147852369'}
delete_database_data(Client, Utilisateur, Demande, Conseiller)
populate = []
populate.append(Client(**data_cli))
populate.append(Admin(**data_admin))
populate.append(Conseiller(**data_conseiller))
populate.append(Demande(**data_demande))

for obj in populate:
    inserer(obj)


client = Client.query.get(2)

print(client.username)
