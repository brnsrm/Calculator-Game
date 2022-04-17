#Zufallsgenerator
import random
random.seed()

#Werte und Berechnungen
a = random.randint(1,10)
b = random.randint(1,10)
c = a + b
print("Die Aufgabe:", a, "+", b)

#Schleife und Anzahl initalisieren
zahl = c + 1
versuch = 0

#Schleife mit while
while zahl != c:
    #Anzahl der Versuche
    versuch = versuch + 1

    #Eingabe
    print("Bitte eine ganze Zahl eingeben:")
    z = input()

        #Versuch einer Umwandlung
    try:
        zahl = int(z)
    except:
        #Falls Umwandlung nicht erfolgreich
        print("Sie haben keine ganze Zahl eingegeben")
        #Schleife unmittelbar fortsetzen
        continue

    #Verzweigungen
    if zahl == c:
        print(zahl, "ist richtig")
        break
    elif zahl < 0 or zahl > 100:
        print(zahl, "ist ganz falsch")
    elif c-1 <= zahl <= c+1:
        print(zahl, "ist ganz nah dran")
    else:
        print(zahl, "ist falsch")

#Anzahl der Versuche
print("Ergebnis:", c)
print("Anzahl Versuche:", versuch)