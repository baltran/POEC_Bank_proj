import modules.bdd as bdd


class Compte:
    def __init__(self, data_compte):
        self.rib, self.proprietaire, self.date_creation, self.solde, self.type = data_compte
        self.__class__.cnx, self.cursor = None, None

    def depot(self, somme, cnx=None):
        if not cnx:
            cnx = bdd.connexion_bdd()
        cursor = cnx.cursor()
        solde_tmp = self.solde + somme
        data = (solde_tmp, self.rib)
        alter_stmt = (
            "Update compte set solde = %s where rib = %s"
        )
        try:
            bdd.envoi_requete(cursor, alter_stmt, data)
        except:
            return -1
        else:
            data = (self.rib, "credit", somme)
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
