import random

class Amazon:
    def __init__(self, prezzo, lista):
        self.prezz = prezzo
        self.vendite = lista
    
    def calcola_vendite(self):
        fatturato_tot = 0
        for i in self.vendite:
            fatturato = i * self.prezz
            fatturato_tot += fatturato
        print("Fatturato totale: ", fatturato_tot)

    def generavendite(self):
        i=1
        while i<4:
            x=random.randint(0,30)
            self.vendite.append(x)
            i+=1
        return self.vendite

class Furgone1(Amazon):
    def __init__(self, prezzo, lista, nome):
        Amazon.__init__(self, prezzo, lista)
        self.nome_f = nome
        
class Furgone2(Amazon):
    def __init__(self, prezzo, lista, nome):
        Amazon.__init__(self, prezzo, lista)
        self.nome_f = nome
    
class Furgone3(Amazon):
    def __init__(self, prezzo, lista, nome):
        Amazon.__init__(self, prezzo, lista)
        self.nome_f = nome

def piccolo_loop(furgone):
    while True:
        opzione = input("V. visualizza vendite e fatturato \nN. azzerra e genera nuove vendite \n0. cambia furgone \n>> ")
        if opzione == "0":
            break
        elif opzione == "V":
            print(furgone.vendite)
            furgone.calcola_vendite()
        elif opzione == "N":
            furgone.vendite = []
            furgone.generavendite()

f1 = Furgone1(4, [3,6,7], "1")
f2 = Furgone2(4, [8,9,1], "2")
f3 = Furgone3(4, [21,4,4], "3")

while True:

    scelta = int(input("Scegli numero furgone: 1, 2, o 3  >>  "))
    if scelta == 1:
        piccolo_loop(f1)
    if scelta == 2:
        piccolo_loop(f2)
    if scelta == 3:
        piccolo_loop(f3)
