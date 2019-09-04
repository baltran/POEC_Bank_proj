import logging
import mysql.connector
import modules.bdd as bdd
from configs.config import DATABASE
logging.basicConfig(filename='connexion.log', level=logging.INFO, format='%(name)s - %(levelname)s - %(message)s')


class Utilisateur:
    #cnx, cursor = bdd.connexion_bdd(database=DATABASE)

    def __init__(self):
        self.login = ""
        self.pwd = ""
        self.nom = ""
        self.prenom = ""
        self.email = ""
        self.email = ""
        self.__class__.cnx, self.cursor = bdd.connexion_bdd(database=DATABASE)

    def connexion(self, login, pwd):
        if not self.__class__.cnx:
            self.__class__.cnx, self.cursor = bdd.connexion_bdd(database=DATABASE)

        requete = "select * from Utilisateur where login=%s and password=PASSWORD(%s)"
        donnees = (login, pwd)
        try:
             bdd.envoi_requete(self.cursor, requete, donnees)
        except mysql.connector.errors.IntegrityError:
            logging.error("Utilisateur inconnu", exc_info=True)
            raise
        else:
            logging.info("connexion réussie")
            self.cursor.fetchone()

    def deconnexion(self,login, pwd):
        pass
