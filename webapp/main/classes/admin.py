import logging
from webapp.main.classes.utilisateur import Utilisateur


class Admin(Utilisateur):

    logging.basicConfig(filename='../log/admin_connexion.log', level=logging.INFO, format='%(name)s - %(levelname)s - %(message)s')

    def __init__(self):
        super().__init__()
        self.demandes = []
        self.agents = []


if __name__== "__main__":
    # cons = Conseiller(data_user, data_conseiller)
    # admin.agents.append(cons)
    # return cons
    admin = Admin()
