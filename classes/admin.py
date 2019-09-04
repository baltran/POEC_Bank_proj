import logging
#import configs.config
import mysql.connector
from  modules.bdd import  envoi_requete, connexion_bdd, fermeture
from classes.utilisateur import Utilisateur


class Admin(Utilisateur):

    logging.basicConfig(filename='../log/admin_connexion.log', level=logging.INFO, format='%(name)s - %(levelname)s - %(message)s')

    def create_agent(self):
        DATABASE = "GestiBankDB"
        #user_admin=Utilisateur()
        cnx_admin, cursor = connexion_bdd(database= DATABASE)

        print("connexion réussie")
        cnx_admin.autocommit = True
        insert_stmt = (
            "INSERT INTO agent (login, date_debut, date_fin ) "
            "VALUES (%s, %s, %s)"
        )
        data = ('pdupont', '2000-12-04', 'null')
        cursor = cnx_admin.cursor()
        cursor.execute(insert_stmt, data)

        cnx_admin.close()







""""if __name__=="__main__":
    def admin_login(self, admin_id, admin_pwd):
        user_admin = Utilisateur()
        cnx_admin, curseur = user_admin.connexion()
        return  cnx_admin
        print("connexion réussie")
        
        
        
        

    admin = Admin()
    admin.admin_login(admin_id='', admin_pwd= '')"""