import logging
import mysql.connector
import re

from modules.bdd import connexion_bdd, envoi_requete, fermeture
from configs.config import DATABASE
logging.basicConfig(filename='connexion.log', level=logging.INFO, format='%(name)s - %(levelname)s - %(message)s')
#logging.config.fileConfig(fname='../configs/log.conf', disable_existing_loggers=False)
# Récupère le logger spécifié dans le fichier
#logger = logging.getLogger(__name__)


#dfgfgh
class Utilisateur:
    def __init__(self, login="", pwd="", nom="", prenom="", email=""):
        self.login = login
        self.pwd = pwd
        self.nom = nom
        self.prenom = prenom
        self.email = email

        self.is_connected = False

    def connexion(self, login, pwd, cnx=None):
        if not cnx:
            cnx = connexion_bdd()
        cursor = cnx.cursor()
        requete = "select login from utilisateur where login=%s and password=PASSWORD(%s)"
        donnees = (login, pwd)
        try:
            envoi_requete(cursor, requete, donnees)
        except mysql.connector.errors.Error:
            logging.error("Utilisateur inconnu", exc_info=True)
            raise
        else:
            result = cursor.fetchone()
            if result:
                logging.info("connexion réussie")
                print(cursor.rowcount)
                print(result)
                login = result[0]

                if login == "admin":
                    role = "admin"
                elif re.match(r"ag\d+", login):
                    role = "conseiller"
                else:
                    role = "client"
                self.is_connected = True
                return role, login
            else:
                return None
        finally:
            cursor.close()

    def deconnexion(self):
        self.is_connected = False
