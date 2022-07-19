# 1. Crea un sistema di calcolo che, dato in input un valore possa modificarlo con somma (Altro input), sottrazione, 
# moltiplicazione e divisione, ripetibile 

def somma(x, y):
    z = x + y
    print(z)

def detrai(x, y):
    z = x - y
    print(z)

def moltiplica(x, y):
    z = x * y
    print(z)

def dividi(x, y):
    z = x / y
    print(z)

while True: 
    scelta = input("Cosa vuoi fare: S - sommare, M - Sottrare, X - Moltiplicare, D - Dividere, altro - per uscire >> ")
    if scelta != "S" and scelta != "M" and scelta != "X" and scelta != "D":
        break
    else: 
        x = int(input("Dammi un numero >> "))
        y = int(input("Dammi un altro numero >> "))
        if scelta == "S":
            somma(x,y)
        elif scelta == "M":
            detrai(x,y)
        elif scelta == "X":
            moltiplica(x,y)
        else:
            dividi(x,y)
