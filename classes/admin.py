import logging
from  configs.config import DATABASE
import mysql.connector
import modules.bdd as bdd
from classes.utilisateur import Utilisateur


class Admin(Utilisateur):

    logging.basicConfig(filename='../log/admin_connexion.log', level=logging.INFO, format='%(name)s - %(levelname)s - %(message)s')

    def __init__(self):
        self.demandes = []
        self.agents = []

    def create_agent(self):

        #user_admin=Utilisateur()
        cnx_admin, cursor = bdd.connexion_bdd()
        cnx_admin.autocommit = True
        insert_stmt = (
            "INSERT INTO agent (mle, login, date_debut, date_fin )"
            "VALUES (%s, %s, %s, %s)"
        )
        data = (1, 'pdupont', '2000-12-04', None)
        cursor = cnx_admin.cursor()
        cursor.execute(insert_stmt, data)


if __name__== "__main__":
    admin = Admin()
    admin.create_agent()