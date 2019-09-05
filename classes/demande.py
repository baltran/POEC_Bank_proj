class Demande():
    def __init__(self):
        self.reponse = ""

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
