from webapp import db
from webapp.main.models import *
from werkzeug.security import generate_password_hash as gph
from webapp.main.requetes import inserer, delete_database_data

data_cli = {'username': 'Baltran', 'password': gph('elpoto'), 'email': 'daubie_vic@msn.com',
            'adresse': '10, rue de la liberté', 'telephone': '0123456789'}
data_admin = {'username': 'admin', 'password': gph('admin'), 'email': 'admin@gestibank.fr'}
delete_database_data(Client, Utilisateur)
u = Client(**data_cli)
admin = Admin(**data_admin)
inserer(admin)
inserer(u)


client = Client.query.get(2)

print(client.username)
