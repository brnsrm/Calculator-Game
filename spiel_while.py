#Zufallsgenerator
import random
random.seed()

#Werte und Berechnung
a = random.randint(1,10)
b = random.randint(1,10)
c = a + b
print("Die Aufgabe:", a, "+", b)

#Schleife initalisieren
zahl = c + 1 # damit nie zahl = c, weil dann Ergbnis automatisch falsch ist 

#Anzahl initalisieren 
versuch = 0

#Schleife mit while
while zahl != c: #!= unendlich so lange du falsche zahl eingibst
    versuch = versuch + 1 #Anzahl Versuche

    #Eingabe mit Umwandlung
    print("Bitte eine Zahl eingeben:")
    z = input()
    zahl = int(z)

#Verzweigung
    if zahl == c:
        print(zahl, "ist richtig")
        #Abbruch
        break
    elif zahl < 0 or zahl > 100:
        print(zahl, "ist ganz falsch")
    elif c-1 <= zahl <= c+1:
        print(zahl, "ist ganz nah dran")
    else:
        print(zahl, "ist falsch")
#Anzahl ausgeben
print("Ergebnis:", c)
print("Anzahl Versuche:", versuch) 