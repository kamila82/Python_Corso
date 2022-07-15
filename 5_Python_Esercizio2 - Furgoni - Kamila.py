import random

class Amazon:
    def __init__(self, name):
        self.nome = name

class Furgone1(Amazon):
    vendite = [3,6,7]
    def __init__(self, prezzo):
        self.prezz = prezzo
        
class Furgone2(Amazon):
    vendite = [8,9,1]
    def __init__(self, prezzo):
        self.prezz = prezzo
    
class Furgone3(Amazon):
    vendite = [21,4,4]
    def __init__(self, prezzo):
        self.prezz = prezzo
    

def calcola_vendite(lista):
    fatturato_tot = 0
    for i in lista:
        fatturato = i*4
        fatturato_tot += fatturato
    print("Fatturato totale: ", fatturato_tot)

def generavendite(lista):
    i=1
    while i<4:
        x=random.randint(0,30)
        lista.append(x)
        i+=1
    return lista

am = Amazon("Amazon")
print("Benvenuto in", am.nome)

while True:
    f1 = Furgone1(4)
    f2 = Furgone2(4)
    f3 = Furgone3(4)
    
    scelta = int(input("Scegli numero furgone: 1, 2, o 3  >>  "))
    if scelta == 1:
        while True:
            opzione = input("V. visualizza vendite e fatturato \nN. azzerra e genera nuove vendite \n0. cambia furgone \n>> ")
            if opzione == "0":
                break
            elif opzione == "V":
                print(f1.vendite)
                calcola_vendite(f1.vendite)
            elif opzione == "N":
                f1.vendite = []
                generavendite(f1.vendite)
    if scelta == 2:
        while True:
            opzione = input("V. visualizza vendite e fatturato \nN. azzerra e genera nuove vendite \n0. cambia furgone \n>> ")
            if opzione == "0":
                break
            elif opzione == "V":
                print(f2.vendite)
                calcola_vendite(f2.vendite)
            elif opzione == "N":
                f2.vendite = []
                generavendite(f2.vendite)
    if scelta == 3:
        while True:
            opzione = input("V. visualizza vendite e fatturato \nN. azzerra e genera nuove vendite \n0. cambia furgone \n>> ")
            if opzione == "0":
                break
            elif opzione == "V":
                print(f3.vendite)
                calcola_vendite(f3.vendite)
            elif opzione == "N":
                f3.vendite = []
                generavendite(f3.vendite)
    print()