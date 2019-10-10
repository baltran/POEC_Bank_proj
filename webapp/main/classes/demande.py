from webapp import db
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
        return {
            'id' : self.id,
            'username' : self.username,
            'nom' : self.nom,
            'prenom' : self.prenom,
            'email' : self.email,
            'tel': self.tel,
            'adresse': self.adresse,
        }
