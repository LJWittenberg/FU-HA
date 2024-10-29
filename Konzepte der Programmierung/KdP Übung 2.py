#Aufgabe 2)a)
Grundseite = float(input("Grundseite eingeben: "))
Höhe = float(input("Höhe eingeben: "))
from string import ascii_lowercase

areatri = (Grundseite * Höhe)/2
print(f"Die Fläche des Dreiecks beträgt: {areatri}")

#Aufgabe 2)b)
n = int(input("Jahreszahl eingeben: "))
if n % 4 == 0:
    istSchaltjahr = True
else:
    istSchaltjahr = False

if istSchaltjahr == True:
    print(f"{n} ist ein Schaltjahr")
else:
    print(f"{n} ist kein Schaltjahr")

#Aufgabe 2)c)
def mersenne_zahl(n):
    return ((1 << n) -1)
n = int(input("Gib mir eine Zahl: "))
(mersenne_zahl(n))

#Aufgabe 2)d)
print(ord('a'))
print(ord('A'))
letter = str(input("Buchstabe eingeben: "))
def buchstabe_umkehren(letter):
    if 'a' <= letter <= 'z':
        return chr(ord(letter) - 32)
    elif 'A' <= letter <= 'Z':
        return chr(ord(letter) + 32)
    else:
        return ("Keine valide Eingabe")
print(buchstabe_umkehren(letter))

#Aufgabe 2)e)
age = int(input("Big dein Alter an: "))
preis1 = 10
preis2 = 12
preis3 = 14
def kinokarte(age):
    if (age <= 12):
        return(preis1)
    elif (12 <= age <= 18):
        return(preis2)
    elif (18 <= age <= 64):
        return(preis3)
    elif (64 <= age):
        return(preis2)
print(f"Der Preis beträgt {kinokarte(age)}€")