import logging
from  configs.config import DATABASE
import mysql.connector
import modules.bdd as bdd
from classes.utilisateur import Utilisateur
from classes.conseiller import Conseiller


class Admin(Utilisateur):

    logging.basicConfig(filename='../log/admin_connexion.log', level=logging.INFO, format='%(name)s - %(levelname)s - %(message)s')

    def __init__(self):
        super().__init__()
        self.demandes = []
        self.agents = []





if __name__== "__main__":
    admin = Admin()
    admin.create_conseiller(('ag1dupont', 'fgfrhfXUkkde$$', 'dupont', 'jean', 'pdupont@gmail.com'), (1, 'ag1dupont', '2000-12-04',  None))
