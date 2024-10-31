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

def Aufgabe_3b():
    n = int(input("Zahl 1: "))
    n_2 = int(input("Zahl 2: "))
    n_3 = int(input("Zahl 3: "))
    paarweiseverschieden = n != n_3 and n != n_2 and n_2 != n_3
    print(paarweiseverschieden) 

def Aufgabe_3c():
    n = int(input("Zahl 1: "))
    n_2 = int(input("Zahl 2: "))
    n_3 = int(input("Zahl 3: "))
    paarweisegleich = n == n_3 and n == n_2 and n_2 == n_3
    print(paarweisegleich)

def Aufgabe_3d_e():
    n = int(input("Zahl 1: "))
    n_2 = int(input("Zahl 2: "))
    n_3 = int(input("Zahl 3: "))
    numbers = set()
    numbers.add(n)
    numbers.add(n_2)
    numbers.add(n_3)
    print(len(numbers))
    # b
    print(len(numbers) == 3)
    # c
    print(len(numbers) == 1)
 

def main():
   #Aufgabe_2a()
   #Aufgabe_2b()
   #Aufgabe_2c()
   #Aufgabe_2d() 
   #Aufgabe_2e()
   #Aufgabe_3b()
   #Aufgabe_3c()
    Aufgabe_3d_e()

main()
