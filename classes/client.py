import mysql.connector

from classes.utilisateur import Utilisateur
import modules.bdd as bdd


class Client(Utilisateur):
    def __init__(self, data_user, data_client):
        super().__init__(*data_user)
        self.num_comptes = []
        self.num_client, self.adresse, self.telephone = data_client

    @classmethod
    def creer(cls, data_user, data_client, data_compte, conseiller, cnx=None):
        if not cnx:
            cnx_client, cursor = bdd.connexion_bdd()
        else:
            cursor = cnx.cursor()
        #cnx_admin, cursor = bdd.connexion_bdd()
        data_user_table = data_user
        cursor = cnx_client.cursor()
        insert_stmt_user = (
            "INSERT INTO utilisateur (login, password, nom, prenom, email )"
            "VALUES (%s, password(%s), %s, %s, %s)"
        )
        try:
            bdd.envoi_requete(cursor, insert_stmt_user, data_user_table)
        except mysql.connector.errors.IntegrityError:
            return -1
        data_client_table = data_client
        insert_stmt = (
            "INSERT INTO client (num_client, login, adresse, telephone)"
            "VALUES (%s, %s, %s, %s)"
        )
        bdd.envoi_requete(cursor, insert_stmt, data_client_table)
        bdd.fermeture(cnx_client, cursor)
        client = Client(data_user, data_client)
        data_compte_table = data_compte
        insert_stmt = (
            "INSERT INTO compte (rib, proprietaire, date_creation, type)"
            "VALUES (%s, %s, %s, %s)"
        )
        bdd.envoi_requete(cursor, insert_stmt, data_compte_table)
        bdd.fermeture(cnx_client, cursor)
        conseiller.clients.append(client)
        return client

    def modifier(self):
        pass

    def changer_password(self, new_password, cnx=None):
        pass

