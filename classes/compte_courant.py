import modules.bdd as bdd
from classes.compte import Compte


class CompteCourant(Compte):
    def __init__(self, data_compte, data_compte_avancee):
        super().__init__(data_compte)
        self.num_compte, self.rib, self.autorisation_decouvert, self.taux_decouvert, self.entree_moyenne = data_compte_avancee
        self.__class__.cnx, self.cursor = None, None

    def retrait(self, somme, cnx=None):
        if not cnx:
            Compte.cnx_client, self.cursor = bdd.connexion_bdd()
        else:
            self.cursor = cnx.cursor()
        solde_tmp = self.solde - somme
        if solde_tmp < 0:
            if not self.autorisation_decouvert:
                return -1
            elif solde_tmp < (self.entree_moyenne * self.taux_decouvert):
                return -1
        #TODO prise en compte nouveau solde et ajout transaction dans la bdd

    def virement(self):
        pass
