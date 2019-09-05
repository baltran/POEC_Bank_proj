import logging
import mysql.connector
import re
from classes.admin import Admin
from classes.conseiller import Conseiller
from classes.client import Client
from modules.bdd import connexion_bdd, envoi_requete, fermeture
from configs.config import DATABASE
#logging.basicConfig(filename='connexion.log', level=logging.INFO, format='%(name)s - %(levelname)s - %(message)s')
logging.config.fileConfig(fname='../configs/log.conf', disable_existing_loggers=False)
# Récupère le logger spécifié dans le fichier
logger = logging.getLogger(__name__)


class Utilisateur:
    #cnx, cursor = bdd.connexion_bdd(database=DATABASE)

    def __init__(self, login="", pwd="", nom="", prenom="", email=""):
        self.login = login
        self.pwd = pwd
        self.nom = nom
        self.prenom = prenom
        self.email = email

        self.__class__.cnx, self.cursor = None, None #bdd.connexion_bdd(database=DATABASE)

    def connexion(self, login, pwd, cnx=None):
        if not cnx:
            self.__class__.cnx, self.cursor = connexion_bdd()
        else:
            self.cursor = cnx.cursor()
        requete = "select * from utilisateur where login=%s and password=PASSWORD(%s)"
        donnees = (login, pwd)
        try:
            envoi_requete(self.cursor, requete, donnees)
        except mysql.connector.errors.Error:
            logging.error("Utilisateur inconnu", exc_info=True)
            raise
        else:
            if self.cursor.rowcount == 1:
                logging.info("connexion réussie")
                print(self.cursor.rowcount)
                result = self.cursor.fetchone()
                print(result)
                if login == "admin":
                    role = Admin()
                elif re.match(r"ag\d+", login):
                    role = Conseiller()
                else:
                    role = Client()
                return role
            else:
                return None

    def deconnexion(self,login, pwd):
        pass
