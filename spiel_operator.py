#Zufallsgenerator
import random
random.seed()

#Werte und Berechnung - a oder b koennen alles zwischen 1 und 10 sein, wird zufaellig gewaehlt
a = random.randint(1,10)
b = random.randint(1,10)
c = a + b
print("Die Aufgabe:", a, "+", b)

#Eingabe
print("Bitte eine Zahl eingeben:")
z = input()
zahl = int(z)

#Merfache Verzweigung, logische Operatoren
#Bedingungen mit mehreren Vergleichoperatoren
if zahl == c:
    print(zahl, "ist richtig")
elif zahl <0 or zahl > 100:
    print(zahl, "ist ganz falsch")
elif c-1 <= zahl <= c+1: #Ergebnis nah dran hier Bedingung mit mehreren Vergleichsoperatoren
    print(zahl, "ist ganz nahe dran")
else:
    print(zahl, "ist falsch")

#Ende
print("Ergebnis:", c)