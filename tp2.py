maroc = {"president": "Mohamed VI", "capitale": "Rabat", "superficie": 710850}
algerie = {"president": "Abdelaziz Bouteflika", "capitale": "Alger", "superficie": 2382000}
tunisie = {"president": "Kaïs Saïd", "capitale": "Tunis", "superficie": 163610}

algerie["president"]="Abdelmajid Tebboune"

dicoPays={"Maroc":maroc, "Algerie":algerie, "Tunisie":tunisie}


etudiants = {
    "etudiant_1":13,
    "etudiant_2":17,
    "etudiant_3":9,
    "etudiant_4":15,
    "etudiant_5":8,
    "etudiant_6":14,
    "etudiant_7":14,
    "etudiant_8":12,
    "etudiant_9":13,
    "etudiant_10":15,
    "etudiant_11":14,
    "etudiant_112":9,
    "etudiant_13":12,
    "etudiant_14":12,
    "etudiant_15":13,
    "etudiant_16":7,
    "etudiant_17":12,
    "etudiant_18":15,
    "etudiant_19":9,
    "etudiant_20":17
}

print(etudiants["etudiant_1"])

def ajout_part(dictio):
    dictio["etudiant_21"]=18
    etudiantAdmis={}
    etudiantNonAdmis={}
    for i in dictio:
        if dictio[i]>=10:
            etudiantAdmis[i]=dictio[i]
        else:
            etudiantNonAdmis[i]=dictio[i]
    print("admis : ", etudiantAdmis)
    print("non admis : ", etudiantNonAdmis)




d = {
    "Adam": [12, 15 , 17],
    "Karim" : [15, 12 , 16],
    "Joshua": [13, 15 , 7]
}

def moy_dico(dicomoy):
    moy=0
    for i in dicomoy:
        for j in dicomoy[i]:
            moy+=j
        moy/=len(dicomoy[i])
        dicomoy[i]=moy
        moy=0
    print(dicomoy)


def fact():
    N=input("envoie un entier stp ")
    facto=1
    for i in range (1,int(N)+1):
        facto*=i
    print(facto)



def tablMulti(n):
    print("n?", n)
    for i in range (1,n+1):
        for j in range(1,n+1):
            print(i*j, end=" ")
        print()

tablMulti(5)



