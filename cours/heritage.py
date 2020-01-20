class DateNaissance:
    def __init__(self,jour,mois,annee):
        self.jour = jour
        self.mois = mois
        self.annee = annee
    def ToString(self):
        #self.jour = str(self.jour)
        #self.mois = str(self.mois)
        #self.annee = str(self.annee)
        print ("Date Naissance","%02d/%02d/%d"%(self.jour,self.mois,self.annee))
        
        d1 = DateNaissance(28,11,1997)
        d1.ToString()
        
        class Personne:
    def __init__(self,nom,prenom,DateNaissance):
        self.nom = nom
        self.prenom = prenom
        self.dateNaissance = DateNaissance
    def afficher(self):
        print("Nom:",self.nom)
        print("Prenom:",self.prenom)
        self.dateNaissance.ToString()
        
        
        p1=Personne("Kouba","Slimane",DateNaissance(28,11,1997))
        p1.afficher()
        P=Personne("Ilyass","Math",DateNaissance(1,7,1982))
        P.afficher()
        
        class Employe(Personne):
    def __init__(self,nom,prenom,dateNaissance,salaire):
        super().__init__(nom,prenom,dateNaissance)
        self.salaire=salaire
    def afficher(self):
        super().afficher()
        print('Salaire:',self.salaire.__round__ (2))
        
        E=Employe("Ilyass","Math",DateNaissance(1,7,1985),7865.548)
        E.afficher()
        
        class Chef(Employe):
    def __init__(self,nom,prenom,dateNaissance,salaire,service):
        super().__init__(nom,prenom,dateNaissance,salaire)
        self.service = service
    def afficher(self):
        super().afficher()
        print('Service:',self.service)
        
        Ch=Chef("Ilyass","Math",DateNaissance(1,7,1988),7865.548,"Ressource humaine")
        Ch.afficher()