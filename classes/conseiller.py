from classes.utilisateur import Utilisateur
from classes.demande import Demande


class Conseiller(Utilisateur):
    def __init__(self, mle, date_debut, date_fin, user):
        super().__init__(user[0], user[1], user[2], user[3],user[4])
        self.mle = mle
        self.date_debut = date_debut
        self.date_fin = date_fin


