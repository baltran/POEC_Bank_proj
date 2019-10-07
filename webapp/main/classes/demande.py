from webapp import db
from webapp.main.classes.utilisateur import Utilisateur


class Demande(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(40), index=True, unique=False)
    prenom = db.Column(db.String(40), index=True, unique=False)
    email = db.Column(db.String(40), index=True, unique=True)
    username = db.Column(db.String(40), index=True, unique=True)
    password = db.Column(db.String(50))
    revenu_mensuel = db.Column(db.Integer, index=True, primary_key=False)
    adresse = db.Column(db.String(100), index=True, unique=True)
    tel = db.Column(db.String(20), index=True, unique=True)
    # """Manquent (?) :
    # -> nombre d’enfants
    # -> situation matrimoniale
    # """
    piece_id = db.Column(db.String(100), index=True, unique=True)
    just_salaire = db.Column(db.String(100), index=True, unique=True)
    just_domicile = db.Column(db.String(100), index=True, unique=True)
    conseiller = db.Column(db.Integer, index=True, unique=True)




    def accepter(self):
        print("""Accepter cette demande? (O/N) Pour quitter veuillez entrer "quitter".""")
        self.reponse = input()
        if self.reponse == "O":
            print("Demande acceptée.")
        elif self.reponse == "N":
            print("Demande refusée")
        elif self.reponse == "quitter":
            print("A bientôt !")
            quit()
        else:
            print("""La réponse doit être O pour "oui" ou N pour "non". Pour quitter veuillez entrer "quitter".""")
            self.accepter()

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

