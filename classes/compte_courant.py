import modules.bdd as bdd
from classes.compte import Compte


class CompteCourant(Compte):
    def __init__(self, data_compte, data_compte_avancee):
        super().__init__(data_compte)
        self.rib, self.proprietaire, self.date_creation, self.solde, self.type = data_compte_avancee
        self.__class__.cnx, self.cursor = None, None

    def retrait(self, somme, cnx=None):
        if not cnx:
            Compte.cnx_client, self.cursor = bdd.connexion_bdd()
        else:
            self.cursor = cnx.cursor()
        solde_tmp = self.solde - somme
        if self.solde_tmp < 0:
            if not self.autorisation_decouvert:
                return -1
            elif solde_tmp < (self.entree_moyenne * self.taux_decouvert):
                return -1

    def virement(self):
        pass
