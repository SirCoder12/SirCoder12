import sys
import math

def Collatz_Konjektur_zahl(zahl):
    liste_aller_schritte = [zahl, ]
    liste_endzahlen = [1, 0, -1, -5, -17]

    while zahl not in liste_endzahlen:
        if zahl % 2 == 0:
            zahl /= 2
            print("/2", zahl)
            liste_aller_schritte.append(zahl)
        else:
            zahl = zahl*3 + 1
            print("*3+1", zahl)
            liste_aller_schritte.append(zahl)
    return liste_aller_schritte
    

def Collatz_Konjektur_potenz(zahl):
    sys.set_int_max_str_digits(int(math.log(zahl, 10) + 641))
    liste_aller_schritte = [zahl, ]
    liste_endzahlen = [1, 0, -1, -5, -17]
    print(zahl)
    
    while zahl not in liste_endzahlen:
        if zahl % 2 == 0:
            zahl = zahl//2
            liste_aller_schritte.append(zahl)
        else:
            zahl = zahl*3 + 1
            liste_aller_schritte.append(zahl)
    return liste_aller_schritte
   

def Collatz_Konjektur_optimiziert(zahl):
    ursprung = zahl
    liste_endzahlen = [1, 0, -1, -5, -17]
    
    while zahl not in liste_endzahlen:
        if zahl < ursprung - 1:
            break
        if zahl % 2 == 0:
            zahl /= 2
        else:
            zahl = zahl*3 + 1
    return ursprung

def Collatz_Konjektur_test(zahl):
    print(zahl)

    while True:
        if zahl % 2 == 0:
            leer_input = input("")
            zahl = zahl/2
            print("/2", zahl)
            if leer_input != "":
                print("Geht nicht")
                break
        else:
            leer_input = input("")
            zahl = zahl*3+1
            print("*3+1", zahl)
            if leer_input != "":
                print("Geht nicht")
                break

def istfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False                    

def main():
    print("""\nDie Collatz Konjektur, ein mathemathisches Problem der Unmöglichkeit
Von Mihail Zabolotnic (michail.zabolotnic@gmail.com)

Hallo Spielender! Willkommen bei der Collatz Konjektur. Bitte wähle aus ob du eine Zahl, mehrere Zahlen, \
eine Potenz, eine Testvariante oder eine Reichweite an Zahlen (1-54) haben willst.""")
    regeln_input = input("""Zuerst einmal: Weißt du was das ist (ja, nein): 
""")
    
    if regeln_input == "nein":
        print("\nBeginne mit irgendeiner natürlichen Zahl n. Ist n gerade, so nimm als nächstes n/2 Ist n ungerade, so nimm als nächstes 3n+1.")
    
    while True:
        liste_valide_eingaben = ["1", "2", "3", "4", "5"]
        modus_input = input("\nzahl(1), potenz(2), liste(3), test(4), reichweite(5) (ctrl+c um aufzuhören): \n")
        
        if modus_input not in liste_valide_eingaben:
            print("Dies ist kein valider Wert")

        elif modus_input == "1":
            zahl_string = input("Bitte gebe deine Zahl ein: ")
            
            while istfloat(zahl_string) == False:
                zahl_string = input("Dies ist kein valider Wert. Bitte gebe deine Zahl ein:")
            
            zahl = float(zahl_string)
            print(zahl)
            liste_schritte = Collatz_Konjektur_zahl(zahl)
            
            print("Du bist gescheitert.")
            print("Anzahl Schritte:", len(liste_schritte)-1)
            print("Größte Zahl:", max(liste_schritte))
            print("Kleinste Zahl:", min(liste_schritte))
        
        elif modus_input == "2":
            zahl_liste = input("Bitte gebe deine Zahlpotenz mit Komma ein:").split(",")

            try:
                zahl=int(zahl_liste[0]) ** int(zahl_liste[1])
                zahl += eval(input("Was willst du an der Potenz ändern? Gebe das Rechenzeichen und den Wert oder nichts ein:"))
            
            except ValueError:
                print("Dies ist kein valider Wert.")
                continue
           
            except SyntaxError:
                pass

            liste_schritte = Collatz_Konjektur_potenz(zahl)
            print("Du bist gescheitert.")
            print("Anzahl Schritte:", len(liste_schritte)-1)
            
        elif modus_input == "3":
            liste_zahlen = input("Bitte gebe deine Zahlen mit Komma ein:").split(",")
            
            for zahl, wert in enumerate(liste_zahlen):
                try:
                    liste_zahlen[zahl] = int(liste_zahlen[zahl]) 
                except ValueError:
                    liste_zahlen.pop(zahl)   

            for zahl, wert in enumerate(liste_zahlen):
                print("\nZahl:", liste_zahlen[zahl])
                Collatz_Konjektur_zahl(liste_zahlen[zahl])        
        
        elif modus_input == "4":
            zahl_string=input("Bitte gebe deine Zahl ein:")
            
            while istfloat(zahl_string) == False:
                zahl_string=input("Dies ist kein valider Wert. Bitte gebe deine Zahl ein:")
            
            zahl = float(zahl_string)
            print(zahl)
            Collatz_Konjektur_test(zahl)

        
        elif modus_input == "5":
            min_zahl = input("Bitte gebe deine minimale Reichweite an:")
            
            while istfloat(min_zahl) == False:
                min_zahl=input("Dies ist kein valider Wert. Bitte gebe deine minimale Reichweite an:")
            
            max_zahl = input("Bitte gebe deine maximale Reichweite an:")
            
            while istfloat(max_zahl) == False:
                max_zahl=input("Dies ist kein valider Wert. Bitte gebe deine maximale Reichweite an:")
            
            min_zahl = int(min_zahl) 
            max_zahl = int(max_zahl) 
            print("Möchtest du optimiziert oder normal für positive oder negative Zahlen?")
            reichweite_modus=input("optimiziert(1), normal(2), -optimiziert(3), -normal(4):")
            
            if reichweite_modus == "1":
                for zahl in range(min_zahl, max_zahl+1):
                    Collatz_Konjektur_optimiziert(zahl)
                    print(f"\nZahl {zahl}: geht nicht.")
            
            elif reichweite_modus == "2":
                for zahl in range(min_zahl, max_zahl+1):
                    print("\nZahl:", zahl)
                    Collatz_Konjektur_zahl(zahl)
            
            elif reichweite_modus == "3":
                while min_zahl != max_zahl-1:
                    Collatz_Konjektur_optimiziert(min_zahl)
                    min_zahl-=1
            
            
            elif reichweite_modus == "4":
                while min_zahl != max_zahl-1:
                    print("\nZahl:", min_zahl)
                    Collatz_Konjektur_zahl(min_zahl)
                    min_zahl-=1
        
main()