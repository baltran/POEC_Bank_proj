from datetime import datetime

from flask import url_for

from webapp import db
from webapp.main.classes.pagination import PaginatedAPIMixin


class Operation(PaginatedAPIMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    done_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    valeur = db.Column(db.Integer)
    compte_id = db.Column(db.Integer, db.ForeignKey('compte.id'))
    compte_bis_id = db.Column(db.Integer, db.ForeignKey('compte.id'))

    def __repr__(self):
        return '<Operation {}>'.format(self.id)

    def afficher(self):
        return {
            'done_at' : self.done_at,
            'valeur' : self.valeur,
            'compte source' : self.compte_src,

        }

    def to_dict(self):
        data = {
            'id': self.id,
            'done_at': self.done_at,
            'valeur': self.valeur,
            'compte_id': self.compte_id
        }
        if self.compte_bis_id:
            data['compte_bis_id'] = self.compte_bis_id
        return data

    def from_dict(self, data):
        for field in ['id', 'done_at', 'valeur', 'compte_id']:
            if field in data:
                setattr(self, field, data[field])
