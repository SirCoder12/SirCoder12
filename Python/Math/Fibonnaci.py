import gc, sys, math

def fibonnaci_zahlen(anfang, stelle):
    
    if stelle > 640:
        sys.set_int_max_str_digits(int(math.log(10, stelle)))
    
    match anfang:
        case "1,2":
            liste_fibonnaci_zahlen = [1,2]
        
        case "1,1":
            liste_fibonnaci_zahlen = [1,1]
        
        case _:
            liste_fibonnaci_zahlen = [0,1]
        
    [print(wert) for wert in liste_fibonnaci_zahlen]
    
    for wert, stelle in enumerate(liste_fibonnaci_zahlen):
        print(wert,stelle)
        fibonnaci_zahl = wert + liste_fibonnaci_zahlen[stelle-1]
        print(f"{fibonnaci_zahl}\n")
        liste_fibonnaci_zahlen.append(fibonnaci_zahl)


def fibonnaci_stelle(anfang, stelle):
    if stelle > 640:
        sys.set_int_max_str_digits(stelle)
    
    if anfang == "2":
        liste_fibonnaci_zahlen=[1,2]
    
    elif anfang == "1":
        liste_fibonnaci_zahlen=[1,1]
    
    else:
        liste_fibonnaci_zahlen=[0,1]
    
    for zahl in range(1, stelle):
        
        if zahl % 10000 == 0:
            gc.collect()               
        
        fibonnaci_zahl=liste_fibonnaci_zahlen[zahl]+liste_fibonnaci_zahlen[zahl-1]
        liste_fibonnaci_zahlen.append(fibonnaci_zahl)
    
    print(f"\n# Die {stelle}ste Stelle ist {liste_fibonnaci_zahlen[stelle]}")

def main():
    try:
        print("""\nDie Fibonacci-Folge, eine der wichtigsten Folgen der Mathematik
Von Mihail Zabolotnic (michail.zabolotnic@gmail.com) (strg+c um aufzuhören)""")
        wissen_input=input("\nKennst du solch eine Folge? (ja, nein):")
        
        if wissen_input == "nein":
            print("""\nEine Folge ist eine Liste von Zahlen die durch eine Formel endlich oder unendlich definiert wird.
Die Fibonnaci-Folge beginnt entweder mit 0,1; 1,1; oder 1,2. 
Danach werden die letzten beiden Zahlen addiert und der Folge hinzugefügt.""")
        while True:
            stelle = input("\nBitte gebe deine Stelle ein:")

            while stelle.isdigit() == False:
                stelle = input("Dies ist kein valider Wert. Bitte gebe deine Stelle ein:")
            
            stelle = int(stelle)
            methode_auswahl = input("Möchtest du eine Stelle oder alle Zahlen bis zur Stelle erfahren (1,2): ")
            anfang = input("Möchtest du bei 0,1; 1,1 oder bei 1,2 anfangen (0,1,2):")
            
            if methode_auswahl == "1":
                fibonnaci_stelle(anfang, stelle)
            
            
            else:
                fibonnaci_zahlen(anfang, stelle)
    except KeyboardInterrupt:
        print("\n\nAuf Wiedersehen!")
        sys.exit()
main()