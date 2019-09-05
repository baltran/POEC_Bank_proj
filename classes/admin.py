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

    def create_conseiller(self):

        cnx_admin, cursor = bdd.connexion_bdd()
        data_user_table = ('ag1dupont', 'fgfrhfXUkkde$$', 'dupont', 'jean', 'pdupont@gmail.com')
        cursor = cnx_admin.cursor()
        insert_stmt_user = (
            "INSERT INTO utilisateur (login, password, nom, prenom, email )"
            "VALUES (%s, password(%s), %s, %s, %s)"
        )
        bdd.envoi_requete(cursor, insert_stmt_user, data_user_table)
        data_agent_table = (1, 'pdupont', 'jean', None)

        insert_stmt = (
            "INSERT INTO agent (mle, login, date_debut, date_fin )"
            "VALUES (%s, %s, %s, %s)"
        )
        bdd.envoi_requete(cursor, insert_stmt, data_agent_table)
        bdd.fermeture(cnx_admin, cursor)
        cons = Conseiller(1, 'pdupont', 'jean', None, ('ag1dupont', 'fgfrhfXUkkde$$', 'dupont', 'jean', 'pdupont@gmail.com'))
        self.agents.append(cons)
        print(self.agents)


if __name__== "__main__":
    admin = Admin()
    admin.create_conseiller()