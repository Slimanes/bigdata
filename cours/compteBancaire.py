class CompteBancaire:
    def __init__(self,nom='Dupont',solde=1000):
        self.nom = nom
        self.solde = solde
    def depot(self,somme):
        self.solde=self.solde + somme
        print("Votre solde est de",self.nom,'est de',self.solde)
    def retrait(self,somme):
        self.solde=self.solde - somme
    def affiche(self):
        print("Le titulaire est du solde est Monsieur",self.nom,'et son solde est de ',self.solde)    
        
compte1 = CompteBancaire(‘Duchmol’, 800)
compte1.depot(350)
compte1.retrait(200)
compte1.affiche()
compte2 = CompteBancaire()
compte2.depot(25)
compte2.affiche()