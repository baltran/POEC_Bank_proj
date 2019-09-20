import logging
import mysql.connector
import re

from werkzeug.security import check_password_hash, generate_password_hash

from modules.bdd import connexion_bdd, envoi_requete, fermeture
from configs.config import DATABASE
from webapp import db

logging.basicConfig(filename='connexion.log', level=logging.INFO, format='%(name)s - %(levelname)s - %(message)s')
#logging.config.fileConfig(fname='../configs/log.conf', disable_existing_loggers=False)
# Récupère le logger spécifié dans le fichier
#logger = logging.getLogger(__name__)


#dfgfgh
class Utilisateur(db.Models):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(40), index=True, unique=True)
    nom = db.Column(db.String(40), index=True, unique=True)
    prenom = db.Column(db.String(40), index=True, unique=True)
    password = db.Column(db.String(50))

    def __repr__(self):
        return '<Utilisateur {}>'.format(self.login)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def set_password(self, password):
        self.password = generate_password_hash(password)


