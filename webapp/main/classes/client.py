#import mysql.connector
from webapp import db
from webapp.main.classes.utilisateur import Utilisateur
from webapp.main.classes.compte import Compte
import modules.bdd as bdd


class Client(Utilisateur):
    __tablename__ = 'client'
    __mapper_args__ = {'polymorphic_identity': 'client'}
    id = db.Column(db.Integer, db.ForeignKey('utilisateur.id'), primary_key=True)
    num_client = db.Column(db.Integer, index=True, unique=True)
    adresse = db.Column(db.String(50))
    tel = db.Column(db.String(10))
    revenu_mensuel = db.Column(db.Float)
    conseiller_id = db.Column(db.Integer, db.ForeignKey('conseiller.id'))
    comptes = db.relationship('Compte', backref='titulaire', lazy='dynamic')

    @classmethod
    def creer(cls, data_user, data_client, data_compte, data_compte_avancee, cnx=None):
        pass

    def modifier(self):
        pass

    def changer_password(self, new_password, cnx=None):
        pass

    def afficher(self):
        super().afficher().update({
            'adresse': self.adresse
        })
        return super().afficher()
