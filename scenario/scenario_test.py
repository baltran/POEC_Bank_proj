from webapp.main.classes.admin import Admin
from webapp.main.classes.conseiller import Conseiller
from webapp.main.classes.utilisateur import Utilisateur


data_user= ('ag1ingrachen', 'hsdzhhhdzkkd222$$', 'ingrachen', 'sadia', 's.sadia@gmail.com', 'conseiller')
data_agent = (3, 'ag1ingrachen', '2003-12-04', None)
Conseiller.creer(data_user, data_agent, 'admin')
