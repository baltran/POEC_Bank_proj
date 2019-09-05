from classes.utilisateur import Utilisateur
from classes.demande import Demande


class Conseiller(Utilisateur):
    def __init__(self, data_user, data_conseiller):

        super().__init__(*data_user)
        self.mle = data_conseiller[0]
        self.date_debut = data_conseiller[2]
        self.date_fin = data_conseiller[3]

