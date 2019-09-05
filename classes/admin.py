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

    def create_conseiller(self, data_user, data_conseiller):
        cnx_admin, cursor = bdd.connexion_bdd()
        data_user_table = data_user
        cursor = cnx_admin.cursor()
        insert_stmt_user = (
            "INSERT INTO utilisateur (login, password, nom, prenom, email )"
            "VALUES (%s, password(%s), %s, %s, %s)"
        )
        try:
            bdd.envoi_requete(cursor, insert_stmt_user, data_user_table)
        except mysql.connector.errors.IntegrityError:
            return -1
        data_agent_table = data_conseiller
        insert_stmt = (
            "INSERT INTO agent (mle, login, date_debut, date_fin )"
            "VALUES (%s, %s, %s, %s)"
        )
        bdd.envoi_requete(cursor, insert_stmt, data_agent_table)
        bdd.fermeture(cnx_admin, cursor)
        cons = Conseiller(data_user, data_conseiller)
        self.agents.append(cons)
        print(self.agents)


if __name__== "__main__":
    admin = Admin()
    admin.create_conseiller(('ag1dupont', 'fgfrhfXUkkde$$', 'dupont', 'jean', 'pdupont@gmail.com'), (1, 'ag1dupont', '2000-12-04',  None))
