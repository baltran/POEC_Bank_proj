import mysql.connector
import modules.bdd as bdd
from classes.utilisateur import Utilisateur
from classes.demande import Demande


class Conseiller(Utilisateur):
    def __init__(self, data_user, data_conseiller):
        super().__init__(*data_user)
        self.mle = data_conseiller[0]
        self.date_debut = data_conseiller[2]
        self.date_fin = data_conseiller[3]

    @classmethod
    def creer(self, data_user, data_conseiller, admin, cnx=None):
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
        admin.agents.append(cons)
        return cons


    def modifier(self, cnx=None):
       pass

    def supprimmer(self, cnx=None):
        pass

