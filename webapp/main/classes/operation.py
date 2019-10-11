from datetime import datetime
from flask import url_for
from webapp import db
from webapp.main.classes.compte import Compte
from webapp.main.classes.pagination import PaginatedAPIMixin
import enum


class TypeOp(enum.Enum):
    depot = 1
    retrait = 2
    virement = 3


class Operation(PaginatedAPIMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    done_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    valeur = db.Column(db.Float)
    type_operation = db.Column(db.Enum(TypeOp))
    label = db.Column(db.String)
    compte_id = db.Column(db.Integer, db.ForeignKey('compte.id'))
    compte_bis_id = db.Column(db.Integer, db.ForeignKey('compte.id'))

    def __repr__(self):
        return '<Operation {}>'.format(self.id)

    def afficher(self):
        compte = Compte.query.get(self.compte_id)
        compte_dest = Compte.query.get(self.compte_bis_id or -1)
        beneficiaire = ""
        if compte_dest:
            beneficiaire = (self.compte_bis.titulaire.nom or "") + " " + \
                       (self.compte_bis.titulaire.prenom or "") + \
                       " (" + compte_dest.discriminator + ")"
        return {
            'Fait le'     : self.done_at or "",
            'Valeur'      : self.valeur or "",
            'Émetteur'    : self.compte_id or "",
            'Type'        : self.type_operation.name or "",
            'Bénéficiaire': self.compte_bis_id or "",
            'Libellé'     : self.label or ""
        }

    def to_dict(self):
        data = {
            'id'            : self.id,
            'done_at'       : self.done_at,
            'valeur'        : self.valeur,
            'compte_id'     : self.compte_id,
            'type_operation': self.type_operation.name,
            'label'         : self.label
        }
        if self.compte_bis_id:
            data['compte_bis_id'] = self.compte_bis_id
        return data

    def from_dict(self, data):
        for field in ['id', 'done_at', 'valeur', 'compte_id', 'type_operation', 'label']:
            if field in data:
                setattr(self, field, data[field])
