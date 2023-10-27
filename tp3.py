import math
def nbChiffresDuCarre(n):
    carre=n*n
    print(len(str(carre)))

def estPremier(n):
    for i in range (2,int(math.sqrt(n))+1):
        if(n%i==0):
            return False
    return True
def listePremier(n):
    for i in range (1,11):
        if(estPremier(i)):
            print(i)




class MaDate:
    def __init__(self, jour, mois, annee):
        self.jour = jour
        self.mois = mois
        self.annee = annee

    def affichage_date(self):
        return str(self.jour) + "/" + str(self.mois) + "/" + str(self.annee)


def creationDate():
    ann=input("Entrez l'année :")
    mo=input("Entrez le mois :")
    jou=input("Entrez le jour: ")
    mo=int(mo)
    jou=int(jou)
    ann=int(ann)
    if(mo>0 and mo<13 and jou>0 and jou<31):
        date1=MaDate(jou, mo, ann);
        return date1
    else :
        print("date inccorect")
        return creationDate()


class Personne:
    def __init__(self, nom, prenom, dateDeNaissance, dateEmbauche):
        self.nom = nom
        self.prenom = prenom
        self.dateDeNaissance = dateDeNaissance
        self.dateEmbauche = dateEmbauche

    def affichage_perso(self):
        print("Personne : ", self.prenom, self.nom)
        print("date de naissance : ")
        print(self.dateDeNaissance.affichage_date())
        print("date d'embauche : ")
        print(self.dateEmbauche.affichage_date())


def creationPersonne():
    nom=input("Entre un nom :")
    prenom=input("Entrez un prenom :")
    print("Entre votre date de naissance")
    dateNaissance=creationDate()
    print("Entrez votre date d'embauche")
    dateEmbauche=creationDate()
    return Personne(nom,prenom,dateNaissance,dateEmbauche)






def estPlusRecenteQue(date1, date2):
    if date1.annee>date2.annee:
        return True
    else:
        if date1.annee==date2.annee:
            if date1.mois>date2.mois:
                return True
            else:
                if date1.mois==date2.mois:
                    if date1.jour>date2.jour:
                        return True
                    else: False
                else: False
        else: False

employe1=creationPersonne()
employe2=creationPersonne()

def quiEstPlusRecent(employe1, employe2):
    if(estPlusRecenteQue(employe1.dateEmbauche,employe2.dateEmbauche)):
        employe1.affichage_perso()
        print("n'a pas plus d'experience que :")
        employe2.affichage_perso()
    else:
        employe1.affichage_perso()
        print("est plus récent que :")
        employe2.affichage_perso()  

quiEstPlusRecent(employe1,employe2)

