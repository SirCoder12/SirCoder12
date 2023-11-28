import math

def Harmonische_Serie(anzahl_brüche):
    liste_brüche=[]
    
    for zahl in range(anzahl_brüche):
        bruch = 1/zahl
        liste_brüche.append(bruch)
        print("+1/", zahl, summe := sum(liste_brüche))
    return liste_brüche, summe

def Harmonische_Serie_alles(anzahl_brüche, limit):
    liste_brüche=[]
    
    for zahl in range(1,limit):
        print("+(1/", zahl, "-1/(", anzahl_brüche, "+", zahl, "))")
        sum = (1/zahl) - (1/(anzahl_brüche + zahl))
        
        print(sum)
        liste_brüche.append(sum)
        print(summe := math.fsum(liste_brüche))
    
    print("Das Ergebnis ist:", math.fsum(liste_brüche))
    return liste_brüche, summe
   
   

def main():
    print("""Die Harmonische Serie, eine simple Summe.
Von Mihail Zabolotnic (michail.zabolotnic@gmail.com) (strg+c um aufzuhören)""")
    while True:
        print("Hallo Spieler! Bitte wähle aus ob du eine ganze oder eine nicht ganze Zahl berechnen willst:")
        checker=input("ganz, reelle:")
        
        if checker == "ganz":
            anzahl_brüche=int(input("Bitte gebe deine Stelle ein:"))
            Harmonische_Serie()
        
        elif checker == "reelle":
            anzahl_brüche=float(input("Bitte gebe deine Stelle ein:"))
            limit=int(input("Bitte gebe dein Limit ein:"))
            Harmonische_Serie_alles(anzahl_brüche, limit)
        
        else:
            print("Dies ist kein valider Wert")
if __name__ == "__main__":
    main()

