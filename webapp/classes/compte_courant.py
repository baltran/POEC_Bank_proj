import modules.bdd as bdd
from webapp.classes.compte import Compte


class CompteCourant(Compte):
    def __init__(self, data_compte, data_compte_avancee):
        super().__init__(data_compte)
        self.num_compte, self.rib, self.autorisation_decouvert, self.taux_decouvert, self.entree_moyenne = data_compte_avancee

    def retrait(self, somme, cnx=None):
        if not cnx:
            cnx = bdd.connexion_bdd()
        cursor = cnx.cursor()
        solde_tmp = self.solde - somme
        if solde_tmp < 0:
            if not self.autorisation_decouvert:
                return -1
            elif solde_tmp < (self.entree_moyenne * self.taux_decouvert):
                return -1
        data = (solde_tmp, self.rib)
        alter_stmt = (
            "Update compte set solde = %s where rib = %s"
        )
        try:
            bdd.envoi_requete(cursor, alter_stmt, data)
        except:
            return -1
        else:
            data = (self.rib, "debit", somme)
            insert_stmt = (
                "INSERT INTO operation (rib_compte, type_opt, valeur)"
                "VALUES (%s, %s, %s)"
            )
            try:
                bdd.envoi_requete(cursor, insert_stmt, data)
            except:
                return -1
        finally:
            cursor.close()

