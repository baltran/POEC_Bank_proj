import mysql.connector

import modules.bdd as bdd
from classes.utilisateur import Utilisateur
from classes.demande import Demande


class Conseiller(Utilisateur):
    def __init__(self, data_user, data_conseiller):
        super().__init__(*data_user)
        self.mle = data_conseiller[0]
        self.date_debut = data_conseiller[2]
        self.date_fin = data_conseiller[3]

    @classmethod
    def creer(self, data_user, data_conseiller, role, cnx=None):
        if role == "admin":
            cnx_admin, cursor = bdd.connexion_bdd()
            data_user_table = data_user
            insert_stmt_user = (
                "INSERT INTO utilisateur (login, password, nom, prenom, email, type)"
                "VALUES (%s, password(%s), %s, %s, %s, %s)"
            )
            try:
                bdd.envoi_requete(cursor, insert_stmt_user, data_user_table)
            except mysql.connector.errors.IntegrityError:
                return -1
            data_agent_table = data_conseiller
            insert_stmt = (
                "INSERT INTO agent (mle, login, date_debut, date_fin )" 
                "VALUES (%s, %s, %s, %s)"
            )
            bdd.envoi_requete(cursor, insert_stmt, data_agent_table)
            bdd.fermeture(cnx_admin, cursor)
        else:
            return -1


    def modifier(self, mle_agent, date_sortie, cnx=None):
        cnx, cursor = bdd.connexion_bdd()
        data = (mle_agent, date_sortie)
        alter_stmt = (
            "Update agent set date_fin = %s where mle = %s"
        )
        try:
            bdd.envoi_requete(cursor, alter_stmt, data)
        except:
            return -1
        bdd.fermeture(cnx, cursor)

    def supprimmer(self, cnx=None):
        pass

if __name__ == "__main__":
    #INSERT INTO `utilisateur` (`login`,`password`,`nom`, `prenom`, `email`) VALUES
    #('ag1dupont', 'hhshdzyyds', 'dupont', 'jean' , 'pdupont@gmail.com');

    cons = Conseiller((1, 'ag1dupont', '2000-12-04', None), ('ag1dupont', '2DF57C81EFE267B70AED6F85772E438ECAEE90A2', 'dupont', 'jean', 'pdupont@gmail.com'))
    cons.modifier(1, '2018-05-20')

