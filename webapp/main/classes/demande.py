from webapp import db
# To convert the binary to pdf import:
import os, base64
# To convert back:
from io import BytesIO
from flask import send_file
from webapp.main.classes.utilisateur import Utilisateur


class Demande(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(40), index=True, unique=False)
    prenom = db.Column(db.String(40), index=True, unique=False)
    email = db.Column(db.String(40), index=True, unique=True)
    username = db.Column(db.String(40), index=True, unique=True)
    password = db.Column(db.String(50))
    adresse = db.Column(db.String(100), index=False, unique=False)
    tel = db.Column(db.String(20), unique=False)
    revenu_mensuel = db.Column(db.Integer, index=False)
    # """Manquent (?) :
    # -> nombre d’enfants
    # -> situation matrimoniale
    # """
    piece_id = db.Column(db.LargeBinary)
    just_salaire = db.Column(db.LargeBinary)
    just_domicile = db.Column(db.LargeBinary)
    conseiller_id = db.Column(db.Integer, db.ForeignKey('conseiller.id'))


    def accepter(self):
        pass

    def afficher(self):
        # with open(os.path.expanduser('~/Desktop/piece_id.pdf'), 'wb') as fout:
        #     piece_id = fout.write(base64.decodebytes(self.piece_id))
        # with open(os.path.expanduser('~/Desktop/just_domicile.pdf'), 'wb') as fout:
        #     just_domicile = fout.write(base64.decodebytes(self.just_domicile))
        # with open(os.path.expanduser('~/Desktop/just_salaire.pdf'), 'wb') as fout:
        #     just_salaire = fout.write(base64.decodebytes(self.just_salaire))

        return {
            'id' : self.id,
            # 'username' : self.username,
            'nom' : self.nom,
            'prenom' : self.prenom,
            'email' : self.email,
            'tel': self.tel,
            'adresse': self.adresse ,
            'revenu_mensuel': self.revenu_mensuel
            #'piece_id': piece_id
            #'just_domicile': just_domicile,
            #'just_salaire': just_salaire
        }
