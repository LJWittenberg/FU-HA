def Aufgabe_2a():
    
    Grundseite = float(input("Grundseite eingeben: "))
    Höhe = float(input("Höhe eingeben: "))

    areatri = (Grundseite * Höhe)/2
    print(f"Die Fläche des Dreiecks beträgt: {areatri}")

def Aufgabe_2b():
    n = int(input("Jahreszahl eingeben: "))
    ist_schaltjahr = n % 4 == 0 and n % 100 != 0 or n % 400 == 0
    print(ist_schaltjahr)

def Aufgabe_2c():
    #Aufgabe 2)c)
    def mersenne_zahl(n):
        return ((1 << n) -1)
    n = int(input("Gib mir eine Zahl: "))
    n = (mersenne_zahl(n))
    print(n)

def Aufgabe_2d():

    letter = str(input("Buchstabe eingeben: "))
    print(chr(ord(letter) + 32))

def Aufgabe_2e():
    age = int(input("Big dein Alter an: "))
    print("10" if age <=12
    else "12" if 12 <= age <= 18
    else "14" if 18 <= age <= 64
    else "10"
    )

def main():
   Aufgabe_2a()
   Aufgabe_2b()
   Aufgabe_2c()
   Aufgabe_2d() 
   Aufgabe_2e()


main()