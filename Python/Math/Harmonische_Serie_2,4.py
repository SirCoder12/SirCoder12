from decimal import Decimal, getcontext
def Harmonische_Serie():
    anzahl_brüche=int(input("Bitte gebe deine Stelle ein:"))
    getcontext().prec=anzahl_brüche
    zahl=1
    liste_brüche=[]
    while zahl < anzahl_brüche+1:
        bruch=Decimal(1/2**zahl)
        liste_brüche.append(bruch)
        print("+1/", "2^", zahl, sum(liste_brüche))
        zahl+=1

Harmonische_Serie()        