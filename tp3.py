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

listePremier(10)

