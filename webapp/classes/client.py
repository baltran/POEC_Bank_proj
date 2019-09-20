import mysql.connector

from webapp.classes.utilisateur import Utilisateur
import modules.bdd as bdd


class Client(Utilisateur):
    def __init__(self, data_user, data_client):
        super().__init__(*data_user)
        self.num_comptes = []
        self.num_client, self.adresse, self.telephone = data_client

    @classmethod
    def creer(cls, data_user, data_client, data_compte, data_compte_avancee, cnx=None):
        if not cnx:
            cnx = bdd.connexion_bdd()
        cursor = cnx.cursor()
        data_user_table = data_user
        insert_stmt_user = (
            "INSERT INTO utilisateur (login, password, nom, prenom, email )"
            "VALUES (%s, password(%s), %s, %s, %s)"
        )
        try:
            bdd.envoi_requete(cursor, insert_stmt_user, data_user_table)
        except mysql.connector.errors.IntegrityError:
            return -1
        except mysql.connector.errors.DataError:
            return -2

        data_client_table = data_client
        insert_stmt = (
            "INSERT INTO client (num_client, login, conseiller, adresse, telephone)"
            "VALUES (%s, %s, %s, %s, %s)"
        )
        try:
            bdd.envoi_requete(cursor, insert_stmt, data_client_table)
        except mysql.connector.errors.IntegrityError:
            return -1
        except mysql.connector.errors.DataError:
            return -2
        client = Client(data_user, data_client)

        data_compte_table = data_compte
        insert_stmt = (
            "INSERT INTO compte (rib, proprietaire, date_creation, type, solde)"
            "VALUES (%s, %s, %s, %s, %s)"
        )
        try:
            bdd.envoi_requete(cursor, insert_stmt, data_compte_table)
        except mysql.connector.errors.IntegrityError:
            return -1
        except mysql.connector.errors.DataError:
            return -2

        data_compte_table = data_compte_avancee
        insert_stmt = (
            "INSERT INTO compte_epargne (num_compte, rib, taux_remuneration, seuil_remuneration)"
            "VALUES (%s, %s, %s, %s)"
        ) if data_compte[-1] == "epargne" else (
            "INSERT INTO compte_courant (num_compte, rib, autorisation_decouvert, taux_decouvert)"
            "VALUES (%s, %s, %s, %s)"
        )
        try:
            bdd.envoi_requete(cursor, insert_stmt, data_compte_table)
        except mysql.connector.errors.IntegrityError:
            return -1
        except mysql.connector.errors.DataError:
            return -2
        cursor.close()

    def modifier(self):
        pass

    def changer_password(self, new_password, cnx=None):
        pass

