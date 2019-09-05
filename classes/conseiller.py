from classes.utilisateur import Utilisateur
from classes.demande import Demande


class Conseiller(Utilisateur):
    def __init__(self, data_user, data_conseiller):

        super().__init__(user[0], user[1], user[2], user[3],user[4])
        self.mle = mle
        self.date_debut = date_debut
        self.date_fin = date_fin


        super().__init__(*data_user)
        self.mle = data_conseiller[0]
        self.date_debut = data_conseiller[2]
        self.date_fin = data_conseiller[3]

