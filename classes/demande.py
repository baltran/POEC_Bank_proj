class Demande():
    def __init__(self, data_demandeur, justificatifs, conseiller):
        self.nom = data_demandeur[0]
        self.prenom = data_demandeur[1]
        self.email = data_demandeur[2]
        self.login = data_demandeur[3]
        self.password = data_demandeur[4]
        self.revenu_mensuel = data_demandeur[5]
        self.adresse = data_demandeur[6]
        self.tel = data_demandeur[7]
        """Manquent (?) :
            -> nombre d’enfants
            -> situation matrimoniale
        """
        self.piece_id = justificatifs[0]
        self.just_salaire = justificatifs[1]
        self.just_domicile = justificatifs[2]


    @classmethod
    def creer(self, data_demandeur, cnx=None):
        cnx_cons, cursor = bdd.connexion_bdd()
        data_demandeur_table = data_demandeur
        cursor = cnx_demandeur.cursor()
        insert_stmt_demand = (
            "INSERT INTO client (login, password, nom, prenom, email, revenu_mensuel, adresse, tel )"
            "VALUES (%s, password(%s), %s, %s, %s, %f, %s, %i)"
        )
        try:
            bdd.envoi_requete(cursor, insert_stmt_user, data_demandeur_table)
        except mysql.connector.errors.IntegrityError:
            return -1

        bdd.envoi_requete(cursor, insert_stmt, data_agent_table)
        bdd.fermeture(cnx_cons, cursor)
        return "Saved"
