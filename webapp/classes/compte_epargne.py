from webapp.classes.compte import Compte
import modules.bdd as bdd


class CompteEpargne(Compte):

    def __init__(self, data_compte, data_compte_epargne):
        super().__init__(data_compte)
        self.num_compte, self.rib , self.plafond, self.seuil_remuneration = data_compte_epargne
        self.__class__.cnx, self.cursor = None, None

    def virement_epargne(self, montant_virement, cnx=None):
        if not cnx:
            Compte.cnx_client, self.cursor = bdd.connexion_bdd()
        else:
            self.cursor = cnx.cursor()
        if self.solde > 0 :
            ancien_solde =self.solde
            self.solde = ancien_solde - montant_virement
        else:
            return -1

    def crediter(self, data_compte, data_compte_epargne, somme_versee, cnx=None):
        if not cnx:
            Compte.cnx, self.cursor = bdd.connexion_bdd()
        else:
            self.cursor = cnx.cursor()
        if self.solde < self.plafond:
            ancien_solde = self.solde
            self.solde = ancien_solde + somme_versee
            data = data_compte_epargne
            insert_stmt = (
                "INSERT INTO operation (num_compte, rib, taux_remuneration, seuil_remuneration)"
                "VALUES (%s, %s, %s, %s)"
            )
            bdd.envoi_requete(self.cursor, insert_stmt, data)
            if data_compte[0] == data_compte_epargne[1]:
                data_table_compte= data_compte
                insert_stmt_compte= (
                    "INSERT INTO compte (rib, propriétaire, date_creation, solde, type)"
                    "VALUES (%s, %s, %s, %s, %s)"
                )
                bdd.envoi_requete(self.cursor, insert_stmt_compte, data_table_compte)
        else:
            return -2

        return self.solde

    def remunerer(self, data_compte, data_compte_epargne, cnx=None):
        if not cnx:
            Compte.cnx_client, self.cursor = bdd.connexion_bdd()
        else:
            self.cursor = cnx.cursor()
        if self.solde > self.seuil_min_remun:
            ancien_solde=self.solde
            # TODO inclure la date dans le calcul  de la rémunération du compte epargne
            montant_remuneration = ((self.solde - self.seuil_min_remun)*2)/(365 * 100)
            compte_epargne = CompteEpargne()
            self.solde = compte_epargne.crediter(montant_remuneration, ancien_solde)

        else:
            return print("solde inférieur au seuil de rémunération")








