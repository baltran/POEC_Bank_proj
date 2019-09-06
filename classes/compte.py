import modules.bdd as bdd


class Compte:
    def __init__(self, data_compte):
        self.rib, self.proprietaire, self.date_creation, self.solde, self.type = data_compte
        self.__class__.cnx, self.cursor = None, None


    def virement(self):
        pass
