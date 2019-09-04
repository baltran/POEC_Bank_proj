import logging
import mysql.connector
from modules.bdd import connexion_bdd, envoi_requete, fermeture
from configs.config import DATABASE
#logging.basicConfig(filename='connexion.log', level=logging.INFO, format='%(name)s - %(levelname)s - %(message)s')
root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)  # or whatever
handler = logging.FileHandler('connexion.log', 'a', 'utf-8')  # or whatever
handler.setFormatter(logging.Formatter('%(name)s - %(levelname)s - %(message)s'))  # or whatever
root_logger.addHandler(handler)

class Utilisateur:
    #cnx, cursor = bdd.connexion_bdd(database=DATABASE)

    def __init__(self):
        self.login = ""
        self.pwd = ""
        self.nom = ""
        self.prenom = ""
        self.email = ""

        self.__class__.cnx, self.cursor = None, None #bdd.connexion_bdd(database=DATABASE)

    def connexion(self, login, pwd, cnx=None):
        if not cnx:
            self.__class__.cnx, self.cursor = connexion_bdd()
        else:
            self.cursor = cnx.cursor()
        requete = "select * from utilisateur where login=%s and password=PASSWORD(%s)"
        #requete = "select * from utilisateur where login='{}' and password=PASSWORD('{}')".format(login, pwd)
        donnees = (login, pwd)
        try:
            envoi_requete(self.cursor, requete, donnees)
            envoi_requete(self.cursor, requete)
        except mysql.connector.errors.IntegrityError:
            logging.error("Utilisateur inconnu", exc_info=True)
            raise
        else:
            logging.info("connexion réussie")
            print(self.cursor.rowcount)
            result = self.cursor.fetchone()
            print(result)
            return result

    def deconnexion(self,login, pwd):
        pass
