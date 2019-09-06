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
    # cons = Conseiller(data_user, data_conseiller)
    # admin.agents.append(cons)
    # return cons
    admin = Admin()
