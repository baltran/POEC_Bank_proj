import modules.bdd as bdd


class Compte:
    def __init__(self, data_compte):
        self.rib, self.proprietaire, self.date_creation, self.solde, self.type = data_compte
        self.__class__.cnx, self.cursor = None, None

    def retrait(self, somme, cnx=None):
        if not cnx:
            Compte.cnx_client, self.cursor = bdd.connexion_bdd()
        else:
            self.cursor = cnx.cursor()
        solde_tmp = self.solde - somme
        if solde_tmp < 0 and not self.autorisation_decouvert:
            pass

    def virement(self):
        pass
