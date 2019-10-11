from datetime import datetime
from webapp import db
import enum

class TypeOp(enum.Enum):
    depot = 1
    retrait = 2
    virement = 3

class Operation(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    done_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    valeur = db.Column(db.Float)
    type_operation= db.Column(db.Enum(TypeOp))
    compte_id = db.Column(db.Integer, db.ForeignKey('compte.id'))
    compte_bis_id = db.Column(db.Integer, db.ForeignKey('compte.id'))

    def __repr__(self):
        return '<Operation {}>'.format(self.id)

    def afficher(self):
        return {
            'done_at' : self.done_at,
            'valeur' : self.valeur,
            'compte source' : self.compte_id,
            'compte bis' : self.compte_bis_id,
            'type operation': self.type_operation.name



        }
