import modules.bdd as bdd
from webapp import db
from webapp.main.classes.compte import Compte


class CompteCourant(Compte):
    __tablename__ = 'compte_courant'
    __mapper_args__ = {'polymorphic_identity': 'compte_courant'}
    id = db.Column(db.Integer, db.ForeignKey('compte.id'), primary_key=True)
    num_compte = db.Column(db.Integer, index=True, unique=True)
    autorisation_decouvert = db.Column(db.Boolean, default=False)
    taux_decouvert = db.Column(db.Float)
    entree_moyenne = db.Column(db.Integer)

    #def __init__(self, data_compte, data_compte_avancee):
    #    super().__init__(data_compte)
    #    self.num_compte, self.rib, self.autorisation_decouvert, self.taux_decouvert, self.entree_moyenne = data_compte_avancee

    def retrait(self, somme, cnx=None):
        pass

