from turtle import *
import random


#Diese Liste befindet sich hier, da sie pro Funktionsaufruf gleich bleiben muss
liste_aller_benutzten_wörter=[]


""""
Struktur des Codes
1. Subfunktionen für Galgenmännchen
    1.1 Funktion für das Anzeigen des richtigen Buchstabens
    1.2 Funktion zum Malen des Galgenmännchen
    1.3 Funktion zum Erhalten eines Wortes
    1.4 Funktion zum erhalten eines schweren Wortes
2. Eigentliche Spielfunktionen
    2.1 Galgenmännchen leicht
    2.2 Galgenmännchen mittel
    2.3 Galgenmännchen schwer
    2.4 Galgenmännchen für zwei Spieler
3. Hauptfunktion zum Leiten des Spiels
""" 


#1. Alle wichtigen Subfunktionen für das Spiel


#Funktion die das angezeigte Wort ändert, wird hier angewendet indem wir ihr alle Variablen als Parameter überreichen
def richtigen_buchstaben_anzeigen(buchstabe,angezeigtes_wort,lösung):
    #Liste zum suchen von mehreren Buchstaben
    liste_aller_vorherigen_positionen=[0]
    anzahl_der_richtigen_buchstaben=lösung.count(buchstabe)
    
    #wiederholen diesen Teil des Codes so oft bis alle richtigen Buchstaben gefunden wurden
    for zahl in range (anzahl_der_richtigen_buchstaben):
        #Wir finden die Position und schreiben sie auf, damit beim nächsten Mal andere Suchparameter gelten. 
        #Falls der Buchstabe nicht am Anfang ist, werden die Suchparameter um 1 addiert damit nicht der selbe Buchstabe gefunden wird. 
        #Ist es am Anfang wird nichts addiert damit nicht bei eins angefangen wird.
        if lösung.find(buchstabe) == 0:
            position_in_der_lösung=0
        
        else:
            position_in_der_lösung=lösung.find(buchstabe,liste_aller_vorherigen_positionen[zahl]+1,len(lösung))
        liste_aller_vorherigen_positionen.append(position_in_der_lösung)       
        
        #danach entfernen wir den Unterstrich aus dem angezeigten Wort und fügen den Buchstaben hinzu
        angezeigtes_wort.pop(position_in_der_lösung)
        angezeigtes_wort.insert(position_in_der_lösung,buchstabe)
        
#Funktion zum Zeichnen des Galgenmännchen
def galgenmännchen_zeichnen(anzahl_der_fehler):
    #Zuerst geben wir Turtle die Höchstgeschwindigkeit und machen sie unsichtbar
    speed(10)
    hideturtle()
    #wir benutzen Rekursion um die Funktion relativ klein zu halten
    if anzahl_der_fehler == 1:
        penup()
        goto(-100,-50)
        pendown()
        forward(100)
        penup()
        goto(-50,-50)
    
    elif anzahl_der_fehler == 2:
        galgenmännchen_zeichnen(1)
        pendown()
        left(90)
        forward(175)
    
    elif anzahl_der_fehler == 3:
        galgenmännchen_zeichnen(2)
        penup()
        right(90)
        pendown()
        forward(75)
    
    elif anzahl_der_fehler == 4:
        galgenmännchen_zeichnen(3)
        right(90)
        forward(25)
    
    elif anzahl_der_fehler == 5:
        galgenmännchen_zeichnen(4)
        penup()
        right(90)
        pendown()
        circle(12.5)
    
    elif anzahl_der_fehler == 6:
        galgenmännchen_zeichnen(5)
        penup()
        left(90)
        forward(25)
        pendown()
        forward(62.5)
    
    elif anzahl_der_fehler == 7:
        galgenmännchen_zeichnen(6)
        penup()
        right(180)
        forward(35)
        right(45)
        pendown()
        forward(35)


    
    elif anzahl_der_fehler ==  8:  
        galgenmännchen_zeichnen(7)
        penup()
        right(180)
        forward(35)
        right(90)
        pendown()
        forward(35)
    
    elif anzahl_der_fehler == 9:
        galgenmännchen_zeichnen(8)
        penup()
        right(180)
        forward(35)
        right(45)
        forward(35)
        left(45)
        pendown()
        forward(30)
    
    elif anzahl_der_fehler == 10:
        galgenmännchen_zeichnen(9)
        penup()
        right(180)
        forward(30)
        left(90)
        pendown()
        forward(30)


def wort_erhalten():
    #Zuerst öffnen wir die Liste der Wörter und wandeln sie in eine Liste um
    with open("galgenmaennchen_woerter.txt") as text:
        liste_wörter=text.read().split()
    
    #Danach generieren wir ein zufälliges Wort 
    wort=random.choice(liste_wörter)
    
    #Falls das Wort sich in der Liste aller Wörter befindet, wird das Wort neu generiert
    while wort in liste_aller_benutzten_wörter:
        wort=random.choice(liste_wörter)
    
    liste_aller_benutzten_wörter.append(wort)
    return wort.lower()


def schweres_wort_erhalten():
    with open("galgenmaennchen_schwere_woerter.txt") as text:
        liste_wörter=text.read().split()
        
    wort=random.choice(liste_wörter)
    
    while wort in liste_aller_benutzten_wörter:
        wort=random.choice(liste_wörter)
    
    liste_aller_benutzten_wörter.append(wort)
    return wort.lower()


#Funktion für leichten Spielmodus
# 10 Striche, Joker für einen Buchstaben von irgendeiner Position, normale Wörter
def galgenmännchen_leicht():
    #Alle Variablen werden hier initialisiert
    lösung=wort_erhalten()
    
    #Wort welches der Spieler sieht
    angezeigtes_wort=[]
    
    #wird benutzt um den richtigen Galgenmächenschritt zu zeichnen
    anzahl_der_fehler=0
    
    #wird benutzt um das Spiel zu beenden
    spiel_verloren=False
    lösung_gefunden=False


    #wird benutzt um alle falschen Buchstaben die man schon hatte anzuzeigen
    liste_aller_versuche=["Benutzte Buchstaben:"]


    #wird benutzt zum überprüfen, ob der Joker schon verwendet wurde
    anzahl_der_joker=1
   
   #Liste zum überprüfen, ob der input regelgemäß ist
    liste_aller_möglichen_buchstaben=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v", "w", "x","y","z"]


    #wir setzen das angezeigte Wort auf die richtige Anzahl der Buchstaben am Anfang.
    [angezeigtes_wort.append("_") for wert in lösung]
        
    #wir überprüfen ob die Lösung gefunden wurde oder ob der Spieler verloren hat   
    while lösung_gefunden == False and spiel_verloren == False:
        
        #Falls der Spieler zu viele Fehler hatte, wird das Spiel abgebrochen
        if anzahl_der_fehler == 10:
            spiel_verloren=True
        
        #Falls das angezeigte Wort dem Ursprungswort entspricht, hat der Spieler gewonnen
        elif list(lösung) == angezeigtes_wort:
            lösung_gefunden=True
        
        if lösung_gefunden == False and spiel_verloren == False:
            #Hier zeigen wir alle benutzten Buchstaben, das ausgefüllte Wort, die Anzahl der Fehler, die Länge und fragen nach dem Spielerinput.
            print("")
            print(angezeigtes_wort)
            print(liste_aller_versuche)
            print("Anzahl Fehler:", anzahl_der_fehler)
            print("Länge des Wortes:", len(lösung))
            buchstabe=input("Buchstabe oder Wort oder Joker:")
            
            #Falls das richtige Wort eingegeben wird, gewinnt man automatisch
            if list(buchstabe) == list(lösung):
                print("Das ist richtig!")
                lösung_gefunden=True


        #Wir testen ob die Eingabe ein valider Buchstabe ist
        if buchstabe in liste_aller_möglichen_buchstaben:
                
            #Wir überprüfen ob der Buchstabe in der Lösung vorhanden ist und, ob er nicht verwendet wurde. 
            # Danach zeigen wir mithilfe der oben gennanten Subfunktion "richtigen_buchstaben_anzeigen" das neue Wort an.
            if buchstabe in lösung and buchstabe not in liste_aller_versuche:
                print("Das ist richtig!")
                richtigen_buchstaben_anzeigen(buchstabe,angezeigtes_wort,lösung)
            
            #Falls der Buchstabe schonmal benutzt wurde, geben wir eine Fehlermeldung
            elif buchstabe in liste_aller_versuche:
                print("Du hattest diesen Buchstaben schonmal.")
            
            #Wenn nicht in der Lösung vorhanden ist, zeichnen wir das Galgenmännchen.
            else:
                print("Das ist leider falsch.")
                anzahl_der_fehler=anzahl_der_fehler+1
                setheading(0)
                galgenmännchen_zeichnen(anzahl_der_fehler)  


        #Ansonsten testen wir ob der Joker eingesetzt wurde und ob es das erste mal ist, wenn ja wird er benutzt       
        elif (buchstabe == "joker" or  buchstabe =="Joker") and (anzahl_der_joker != 0):
            joker=input("Gebe die Stelle ein die du erfahren möchtest. Beachte dabei, dass es eine valide Stelle ist, die du noch nicht kennst:")
            
            #wir überprüfen ob der Input eine Stelle ist die nicht verwendet wurde oder eine Zahl ist oder ob die Zahl zu groß ist oder die Zahl zu klein ist, wenn ja geben wir eine Fehlermeldung zurück
            while (joker in angezeigtes_wort) or (joker.isdigit()) == False or len(lösung) < int (joker) or int(joker) < 1:
                joker=input("Dies ist kein valider Wert:")


            #Der Joker wird in eine Zahl umgewandelt und um 1 verringert, weil Indexe bei 0 anfangen.
            # Außerdem wird die Anzahl der Joker auf 0 gesetzt
            anzahl_der_joker=0
            joker_zahl=int(joker)-1


            #Jetzt setzen wir die Variable "buchstabe" auf den gewünschten Buchstaben und führen die Subfunktion "richtigen_buchstaben_anzeigen" aus
            buchstabe=lösung[joker_zahl]
            richtigen_buchstaben_anzeigen(buchstabe,angezeigtes_wort,lösung)


        #Wenn es der Joker ist, es aber nicht das erste mal ist, geben wir eine Fehlermeldung
        elif (buchstabe == "joker" or buchstabe == "Joker") and anzahl_der_joker == 0:
            print("Du hast deinen Joker schon verwendet")
        
        #Ansonsten geben wir eine Fehlermeldung
        else:
            print("Dies ist kein valider Wert")
        #Falls der Buchstabe zum erstenmal verwendet wird, fügen wir ihn in die Liste aller Versuche hinzu
        if buchstabe not in liste_aller_versuche and buchstabe in liste_aller_möglichen_buchstaben:
            liste_aller_versuche.append(buchstabe) 
    
    if lösung_gefunden == True:
        print("")
        print(lösung)
        print("Glückwunsch! Du hast das Spiel gewonnen")
    else:
        print("")
        print("Es tut mir leid, aber du hast das Spiel verloren!")
        print("Die Lösung war:", lösung)


#Funktion für mittleren Spielmodus
#10 Striche, kein Joker, normale Wörter


def galgenmännchen_mittel():
    #Alle Variablen werden hier initialisiert
    lösung=wort_erhalten()
    
    #Wort welches der Spieler sieht
    angezeigtes_wort=[]
    
    #wird benutzt um den richtige Galgenmächenschritt zu zeichnen
    anzahl_der_fehler=0
    
    #wird benutzt um das Spiel zu beenden
    spiel_verloren=False
    lösung_gefunden=False


    #wird benutzt für alle falschen Buchstaben
    liste_aller_versuche=["Benutzte Buchstaben:"]
   
   #Liste zum überprüfen, ob der input regelgemäß ist
    liste_aller_möglichen_buchstaben=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v", "w", "x","y","z"]


    
    #wir setzen das angezeigte Wort auf die richtige Anzahl der Buchstaben am Anfang einmal.
    [angezeigtes_wort.append("_") for wert in lösung]


   
    #wir überprüfen ob die Lösung gefunden wurde oder ob der Spieler verloren hat   
    while lösung_gefunden == False and spiel_verloren == False:
        
        #Falls der Spieler zu viele Fehler hatte, wird das Spiel abgebrochen
        if anzahl_der_fehler == 10:
            spiel_verloren=True
        
        #Falls das angezeigte Wort dem Ursprungswort entspricht, hat der Spieler gewonnen
        elif list(lösung) == angezeigtes_wort:
            lösung_gefunden=True
        
        if lösung_gefunden == False and spiel_verloren == False:
            #Hier zeigen wir alle benutzten Buchstaben, das ausgefüllte Wort, die Anzahl der Fehler und fragen nach dem Buchstaben.
            print("")
            print(angezeigtes_wort)
            print(liste_aller_versuche)
            print("Anzahl Fehler:", anzahl_der_fehler)
            print("Länge des Wortes:", len(lösung))
            buchstabe=input("Buchstabe oder Wort:")
            #Falls das richtige Wort eingegeben wird, gewinnt man automatisch
            
            if list(buchstabe) == list(lösung):
                print("Das ist richtig!")
                lösung_gefunden=True
        
        #Wir testen ob die Eingabe ein valider Buchstabe ist
        if buchstabe in liste_aller_möglichen_buchstaben:
                
            #Wir überprüfen ob der Buchstabe in der Lösung, wie oft, vorhanden ist und, ob er nicht verwendet wurde. Danach zeigen wir mithilfe der oben gennanten Methode das neue Wort 
            if buchstabe in lösung and buchstabe not in liste_aller_versuche:
                print("Das ist richtig!")
                richtigen_buchstaben_anzeigen(buchstabe,angezeigtes_wort,lösung)
                        
            #Falls der Buchstabe schonmal benutzt wurde, geben wir eine Fehlermeldung
            elif buchstabe in liste_aller_versuche:
                print("Du hattest diesen Buchstaben schonmal.")
            
            #Wenn nicht, zeichnen wir das Galgenmännchen, und fügen den Buchstabe an die Liste der Versuche falls der Buchstabe das erste Mal falsch ist
            else:
                print("Das ist leider falsch.")
                anzahl_der_fehler=anzahl_der_fehler+1
                setheading(0)
                galgenmännchen_zeichnen(anzahl_der_fehler)


        #Ansonsten geben wir eine Fehlermeldung
        else:
            print("Dies ist kein valider Wert")
        
        #Falls der Buchstabe zum erstenmal verwendet wird, fügen wir ihn in die Liste aller Versuche hinzu
        if buchstabe not in liste_aller_versuche and buchstabe in liste_aller_möglichen_buchstaben:
            liste_aller_versuche.append(buchstabe) 
    
    if lösung_gefunden == True:
        print("")
        print("Glückwunsch! Du hast das Spiel gewonnen")
        print(lösung)
    else:
        print("")
        print("Es tut mir leid, aber du hast das Spiel verloren!")
        print("Die Lösung war:", lösung)


#10 Striche, kein Joker, schwere Wörter
def galgenmännchen_schwer():
    #Alle Variablen werden hier initialisiert
    lösung=schweres_wort_erhalten()
    
    #Wort welches der Spieler sieht
    angezeigtes_wort=[]
    
    #wird benutzt um den richtige Galgenmächenschritt zu zeichnen
    anzahl_der_fehler=0
    
    #wird benutzt um das Spiel zu beenden
    spiel_verloren=False
    lösung_gefunden=False


    #wird benutzt für alle falschen Buchstaben
    liste_aller_versuche=["Benutzte Buchstaben:"]
   
   #Liste zum überprüfen, ob der input regelgemäß ist
    liste_aller_möglichen_buchstaben=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v", "w", "x","y","z"]
    
    #wir setzen das angezeigte Wort auf die richtige Anzahl der Buchstaben am Anfang einmal.
    [angezeigtes_wort.append("_") for wert in lösung]
    
    #wir überprüfen ob die Lösung gefunden wurde oder ob der Spieler verloren hat   
    while lösung_gefunden == False and spiel_verloren == False:
        
        #Falls der Spieler zu viele Fehler hatte, wird das Spiel abgebrochen
        if anzahl_der_fehler == 10:
            spiel_verloren=True
        
        #Falls das angezeigte Wort dem Ursprungswort entspricht, hat der Spieler gewonnen
        elif list(lösung) == angezeigtes_wort:
            lösung_gefunden=True
        
        if lösung_gefunden == False and spiel_verloren == False:
            #Hier zeigen wir alle benutzten Buchstaben, das ausgefüllte Wort, die Anzahl der Fehler und fragen nach dem Buchstaben.
            print("")
            print(angezeigtes_wort)
            print(liste_aller_versuche)
            print("Anzahl Fehler:", anzahl_der_fehler)
            print("Länge des Wortes:", len(lösung))
            buchstabe=input("Buchstabe oder Wort:")
            
            #Falls das richtige Wort eingegeben wird, gewinnt man automatisch
            if list(buchstabe) == list(lösung):
                print("Das ist richtig!")
                lösung_gefunden=True
        
        
        #Wir testen ob die Eingabe ein valider Buchstabe ist
        if buchstabe in liste_aller_möglichen_buchstaben:
                
            #Wir überprüfen ob der Buchstabe in der Lösung, wie oft, vorhanden ist und, ob er nicht verwendet wurde. Danach zeigen wir mithilfe der oben gennanten Methode das neue Wort 
            if buchstabe in lösung and buchstabe not in liste_aller_versuche:
                print("Das ist richtig!")
                richtigen_buchstaben_anzeigen(buchstabe,angezeigtes_wort,lösung)
                        
            #Falls der Buchstabe schonmal benutzt wurde, geben wir eine Fehlermeldung
            elif buchstabe in liste_aller_versuche:
                print("Du hattest diesen Buchstaben schonmal.")
            
            #Wenn nicht, zeichnen wir das Galgenmännchen, und fügen den Buchstabe an die Liste der Versuche falls der Buchstabe das erste Mal falsch ist
            else:
                print("Das ist leider falsch.")
                anzahl_der_fehler=anzahl_der_fehler+1
                setheading(0)
                galgenmännchen_zeichnen(anzahl_der_fehler)   


        #Ansonsten geben wir eine Fehlermeldung
        else:
            print("Dies ist kein valider Wert")
        #Falls der Buchstabe zum erstenmal verwendet wird, fügen wir ihn in die Liste aller Versuche hinzu
        if buchstabe not in liste_aller_versuche and buchstabe in liste_aller_möglichen_buchstaben:
            liste_aller_versuche.append(buchstabe) 
    
    if lösung_gefunden == True:
        print("")
        print("Glückwunsch! Du hast das Spiel gewonnen")
        print(lösung)
    else:
        print("")
        print("Es tut mir leid, aber du hast das Spiel verloren!")
        print("Die Lösung war:", lösung)


def galgenmännchen_zwei_spieler(steller, spieler, löser):
    #Wir fragen nach der Lösung. Danach printen wir Leerzeichen, damit die Lösung unbekannt bleibt.
    print("Bitte gebe dein Wort ein,", spieler[steller],". Bitte beachte dabei das es nur die 26 Buchstaben des Alphabetes enthält:")
    lösung=input("").lower()
    [print("") for zahl in range(20)]    
    
    #Hier werden alle Variablen initialisiert
    
    #Wort welches der Spieler sieht
    angezeigtes_wort=[]
    
    #wird benutzt um den richtige Galgenmächenschritt zu zeichnen
    anzahl_der_fehler=0
    
    #wird benutzt um das Spiel zu beenden
    spiel_verloren=False
    lösung_gefunden=False
    
    #wird benutzt für alle falschen Buchstaben
    liste_aller_versuche=["Benutzte Buchstaben:"]
   
    #Liste zum überprüfen, ob der input regelgemäß ist
    liste_aller_möglichen_buchstaben=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v", "w", "x","y","z"]
    
    #wir setzen das angezeigte Wort auf die richtige Anzahl der Buchstaben am Anfang einmal.
    [angezeigtes_wort.append("_") for wert in lösung]
    
    #wir überprüfen ob die Lösung gefunden wurde oder ob der Spieler verloren hat
    while spiel_verloren == False and lösung_gefunden == False:
        
        #Falls der Spieler zu viele Fehler hatte, wird das Spiel abgebrochen
        if anzahl_der_fehler == 10:
            spiel_verloren = True
       
        #Falls das angezeigte Wort dem Ursprungswort entspricht, hat der Spieler gewonnen
        elif list(lösung) == angezeigtes_wort:
            lösung_gefunden = True
        
        if spiel_verloren == False and lösung_gefunden == False:
            #Hier zeigen wir alle benutzten Buchstaben, das ausgefüllte Wort, die Anzahl der Fehler und fragen nach dem Buchstaben.
            print("")
            print(angezeigtes_wort)
            print(liste_aller_versuche)
            print("Anzahl Fehler:", anzahl_der_fehler)
            print("Länge des Wortes:", len(lösung))
            print(spieler[löser])
            buchstabe=input("Bitte gebe ein Buchstabe oder das Wort ein:")
            
            #Falls das richtige Wort eingegeben wird, gewinnt man automatisch
            if list(buchstabe) == list(lösung):
                lösung_gefunden=True


        #Wir testen ob die Eingabe ein valider Buchstabe ist
        if buchstabe in liste_aller_möglichen_buchstaben:
                
            #Wir überprüfen ob der Buchstabe in der Lösung, wie oft, vorhanden ist und, ob er nicht verwendet wurde. Danach zeigen wir mithilfe der oben gennanten Methode das neue Wort 
            if buchstabe in lösung and buchstabe not in liste_aller_versuche:
                print("Das ist richtig!")
                richtigen_buchstaben_anzeigen(buchstabe,angezeigtes_wort,lösung)
                        
            #Falls der Buchstabe schonmal benutzt wurde, geben wir eine Fehlermeldung
            elif buchstabe in liste_aller_versuche:
                print("Du hattest diesen Buchstaben schonmal.")
            
            #Wenn nicht, zeichnen wir das Galgenmännchen, und fügen den Buchstabe an die Liste der Versuche falls der Buchstabe das erste Mal falsch ist
            else:
                print("Das ist leider falsch.")
                anzahl_der_fehler=anzahl_der_fehler+1
                setheading(0)
                galgenmännchen_zeichnen(anzahl_der_fehler)   


        #Ansonsten geben wir eine Fehlermeldung
        else:
            print("Dies ist kein valider Wert")
        
        #Falls der Buchstabe zum erstenmal verwendet wird, fügen wir ihn in die Liste aller Versuche hinzu
        if buchstabe not in liste_aller_versuche and buchstabe in liste_aller_möglichen_buchstaben:
            liste_aller_versuche.append(buchstabe) 
          
    clear()    
    if spiel_verloren == True:
        print("")
        print("Du hast verloren", spieler[löser])
        print("Du hast gewonnen", spieler[steller])
        print("Die Lösung war:", lösung)
        return True
    
    else:
        print("")
        print(lösung)
        print("Du hast verloren", spieler[steller])
        print("Du hast gewonnen", spieler[löser])
        return False


def main():
    anzahl_spieler=input("Ein oder zwei Spieler? Gebe 1,2 ein:")


    while anzahl_spieler.isdigit() == False:
        anzahl_spieler=input("Dies ist kein valider Wert. Gebe 1,2 ein:")
    
    anzahl_spieler=int(anzahl_spieler)
    name=input("Bitte gebe deinen Namen ein:")
    print("Hallo,", name, ", Willkommen bei Galgenmännchen! Kennst du die Regeln?")
    regeln_input=input("Bitte gebe nichts für ja, oder nein für nein ein:" )


    if regeln_input == "nein":
        print("Je nach Spielmodus überlegt sich entweder der Computer oder der gegnerische Spieler ein Wort, das nicht angezeigt wird.")
        print("Alle Buchstaben des ausgedachten Wortes werden nur durch Striche angezeigt. Der Spieler nennt nun in beliebiger Reihenfolge nacheinander einzelne Buchstaben des Alphabets.")
        print("Der Computer muss nun jeweils anzeigen, wie oft und an welcher Stelle des Lösungswortes der Buchstabe vorkommt. So ergibt sich nach und nach das gesuchte Wort.")
        print("Kommt ein genannter Buchstabe darin jedoch nicht vor oder hat der Löser gar das falsche Wort geraten, so beginnt der erste Spieler damit, einen Galgen mit einem Gehängten zu zeichnen.")
        print("Dies geschieht in mehreren Etappen (bei jeder Fehlfrage kommt ein Teilstrich dazu), so dass der Rätsellöser je nach gespieltem Schwierigkeitsgrad etwa 10 bis 15 Fehlversuche hat.")
        print("Hat er dann das Wort noch nicht herausgefunden, so hat er verloren und hängt symbolisch am Galgen.")
    
    if anzahl_spieler == 2:
        print("Kennt ihr die Regeln für zwei Leute?")
        regeln_zwei_spieler_input=input("Bitte gebe nichts für ja, oder nein für nein ein:")


        if regeln_zwei_spieler_input == "nein":
            print("Einer von euch ist der Steller. Er stellt das gesuchte Wort und organiziert das Spiel. Spieler 1 ist immer zuerst der Steller.")
            print("Der andere ist der Löser. Er muss das Wort erraten.  Man sucht sich aus wieviele Spiele gespielt werden. Die Rollen werden nach jedem Spiel getauscht. Der Spieler mit den meisten Siegen ist der Gewinner.")
        
        spieler_1=input("Bitte gebe deinen Namen ein Spieler 1:")
        spieler_2=input("Bitte gebe deinen Namen ein Spieler 2:")
        spieler={"Spieler 1": spieler_1, "Spieler 2": spieler_2}
        anzahl_runden=input("Wie viele Runden wollt ihr spielen?:")


        while anzahl_runden.isdigit() == False:
            anzahl_runden=input("Dies ist kein valider Wert. Wieviele Runden wollt ihr spielen?:")


        anzahl_runden=int(anzahl_runden)
        
        resultate={"Gewinne Spieler 1:": 0, "Verluste Spieler 1:": 0, "Gewinne Spieler 2:": 0, "Verluste Spieler 2:": 0}
        
        for zahl in range(anzahl_runden):
            if zahl % 2 == 0:
                steller="Spieler 1"
                löser="Spieler 2"
            else:
                steller="Spieler 2"
                löser="Spieler 1"


            if galgenmännchen_zwei_spieler(steller,spieler,löser) == False:
                if löser == "Spieler 1":
                    resultate["Gewinne Spieler 1:"]=resultate["Gewinne Spieler 1:"]+1
                    resultate["Verluste Spieler 2:"]=resultate["Verluste Spieler 2:"]+1
                else:
                    resultate["Verluste Spieler 1:"]=resultate["Verluste Spieler 1:"]+1
                    resultate["Gewinne Spieler 2:"]=resultate["Gewinne Spieler 2:"]+1
            else:
                if steller == "Spieler 1":
                        resultate["Gewinne Spieler 1:"]=resultate["Gewinne Spieler 1:"]+1
                        resultate["Verluste Spieler 2:"]=resultate["Verluste Spieler 2:"]+1
                else:
                    resultate["Verluste Spieler 1:"]=resultate["Verluste Spieler 1:"]+1
                    resultate["Gewinne Spieler 2:"]=resultate["Gewinne Spieler 2:"]+1
            print(resultate)
        
        if resultate["Gewinne Spieler 1:"] == resultate["Gewinne Spieler 2:"]:
            print("Unentschieden")
        
        elif resultate["Gewinne Spieler 1:"] > resultate["Gewinne Spieler 2:"]:
            print("Du hast gewonnen Spieler 1")
        
        else:
            print("Du hast gewonnen Spieler 2")


        
    else:
        schwierigkeitsgrad_regeln=input("Kennst du die Schwierigkeitsgrade? Nichts für ja, nein für nein:")
        
        if schwierigkeitsgrad_regeln == "nein":
            print("Es gibt drei Schwierigkeitsgrade. Bei leicht kriegst du einen Joker für einen Buchstaben von irgendeiner Position und normale Wörter")
            print("Bei mittel kriegst du keinen Joker und normale Wörter")
            print("Bei schwer hingegen kriegst du keinen Joker und schwerere Wörter")
        
        ende=" "
        
        while ende != "nein":
            auswahl_schwierigkeit=input("Bitte wähle deinen Schwierigkeitsgrad zwischen leicht, mittel, schwer aus: ")
            
            if auswahl_schwierigkeit == "leicht":
                galgenmännchen_leicht()
            
            elif auswahl_schwierigkeit == "mittel":
                galgenmännchen_mittel()
            
            elif auswahl_schwierigkeit == "schwer":
                galgenmännchen_schwer()
            ende=input("Möchtest du noch eine Runde spielen? Nichts für ja, nein für nein:")


main()
