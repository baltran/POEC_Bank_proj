from webapp import db
from webapp.main.classes.utilisateur import Utilisateur


class Demande(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(40), index=True, unique=False)
    prenom = db.Column(db.String(40), index=True, unique=False)
    email = db.Column(db.String(40), index=True, unique=True)
    username = db.Column(db.String(40), index=True, unique=True)
    password = db.Column(db.String(50))
    adresse = db.Column(db.String(100), index=True, unique=True)
    tel = db.Column(db.String(20), index=True, unique=True)
    revenu_mensuel = db.Column(db.Integer, index=True, primary_key=False)
    # """Manquent (?) :
    # -> nombre d’enfants
    # -> situation matrimoniale
    # """
    piece_id = db.Column(db.String(100), index=True, unique=True)
    just_salaire = db.Column(db.String(100), index=True, unique=True)
    just_domicile = db.Column(db.String(100), index=True, unique=True)
    conseiller = db.Column(db.Integer, index=True, unique=True)


    def accepter(self):
        pass

    def afficher(self):
        return {
            'id' : self.id,
            'username' : self.username,
            'nom' : self.nom,
            'prenom' : self.prenom,
            'email' : self.email,
        }
