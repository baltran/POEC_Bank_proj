from webapp import db
from webapp.main.models import *
from werkzeug.security import generate_password_hash as gph
from webapp.main.requetes import inserer, delete_database_data

data_cli = {'username': 'Baltran', 'password': 'elpoto', 'email': 'daubie_vic@msn.com', 'conseiller_id': 2,
            'adresse': '10, rue de la liberté', 'tel': '0123456789', 'prenom': 'Victor', 'nom': 'Daubié'}
data_cli_2 = {'username': 'Sadia', 'password': 'Sadia', 'email': 'sadia_ing@msn.com', 'conseiller_id': 2,
              'adresse': '12, rue de la liberté', 'tel': '0123786589', 'prenom': 'Sadia', 'nom': 'Anon'}
data_admin = {'username': 'admin', 'password': 'admin', 'email': 'admin@gestibank.fr'}

data_conseiller = {'username': 'Bob', 'password': 'bob', 'email': 'bob@bip.fr', 'prenom': 'Jean', 'nom': 'Durt'}

data_demande = {'username': 'Bernard', 'password': 'bernard', 'email': 'bern@bip.fr', 'tel': '0147852369'}
data_demande2 = {'username': 'Jean', 'password': 'jean', 'email': 'abd@bip.fr', 'tel': '0145879632'}

data_compte_courant = {'solde': '2600', 'titulaire_id': '2'}
data_compte_courant_2 = {'solde': '1300', 'titulaire_id': '3'}
data_compte_epargne = {'solde': '12600', 'titulaire_id': '2'}
# data_compte_epargne ={'solde': '20400', 'titulaire_id': '1'}

data_virement = {'valeur': 200, 'compte_id': '2', 'compte_bis_id': '1', 'type_operation': 'virement'}
data_virement_2 = {'valeur': 200, 'compte_id': '1', 'compte_bis_id': '2', 'type_operation': 'virement'}
data_depot = {'valeur': 50, 'compte_id': '2', 'type_operation': 'depot'}

delete_database_data(Client, Utilisateur, Demande, Conseiller, CompteCourant, CompteEpargne, Operation)
populate = []
populate.append(Admin(**data_admin))
populate.append(Conseiller(**data_conseiller))
populate.append(Client(**data_cli))
populate.append(Client(**data_cli_2))
populate.append(Demande(**data_demande))
populate.append(Demande(**data_demande2))
populate.append(Operation(**data_virement))
populate.append(Operation(**data_virement_2))
populate.append(Operation(**data_depot))
populate.append(CompteCourant(**data_compte_courant))
populate.append(CompteCourant(**data_compte_courant_2))
populate.append(CompteEpargne(**data_compte_epargne))

for obj in populate:
    inserer(obj)

client = Client.query.get(3)

print(client.username)
compte = Compte.query.get(2)
page = 1
per_page = 5
operations = compte.operations.union_all(compte.virements)

for op in operations:
    print(op.afficher())
