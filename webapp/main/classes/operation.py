from datetime import datetime
from webapp import db


class Operation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    done_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    valeur = db.Column(db.Integer)
    compte_id = db.Column(db.Integer, db.ForeignKey('compte.id'))
    compte_bis_id = db.Column(db.Integer, db.ForeignKey('compte.id'))
    operations = db.relationship('Compte', foreign_keys=[compte_id])
    virements= db.relationship('Compte', foreign_keys=[compte_bis_id])

    def afficher(self):
        return {
            'done_at' : self.done_at,
            'valeur' : self.valeur,
            'compte source' : self.compte_src,

        }
