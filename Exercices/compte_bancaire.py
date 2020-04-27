class CompteBancaire:

    def __init__(self, nom_compte, solde):
        self.nom_compte = nom_compte
        self.solde = solde

    def depot(self, montant):
        self.solde = self.solde + montant

    def retrait(self, montant):
        if (self.solde < montant):
            print("Solde insuffisant pour faire un retrait...")
        else:
            self.solde = self.solde - montant

    def affiche(self):
        print("Le solde du compte bancaire de", self.nom_compte, "est de", self.solde, "€.")

# Test compte fonctionnel
compte1 = CompteBancaire("Dupont", 200)
compte1.depot(300)
compte1.retrait(250)
compte1.affiche()

# Test solde insuffisant pour retrait
compte2 = CompteBancaire ("Jean", 200)
compte2.depot(100)
compte2.retrait(350)
compte2.affiche()