from webapp.main.classes.admin import Admin
from webapp.main.classes.conseiller import Conseiller
from webapp.main.classes.utilisateur import Utilisateur
from webapp.main import models, requetes
from datetime import datetime

# #data_user= ('ag1ingrachen', 'hsdzhhhdzkkd222$$', 'ingrachen', 'sadia', 's.sadia@gmail.com', 'conseiller')
# data_agent = (3, 'ag1ingrachen', '2003-12-04', None)
# Conseiller.creer(data_user, data_agent, 'admin')

requetes.delete_database_data(Conseiller)
data_conseiller ={'username': 'conseiller1', 'email': 'pierre.dupont@mail.com'}
c= models.Conseiller(**data_conseiller)
requetes.inserer(c)

data_admin ={'username': 'admin', 'password': 'admin'}
u = models.Utilisateur(**data_admin)
u.set_password(u.password)
requetes.inserer(u)
