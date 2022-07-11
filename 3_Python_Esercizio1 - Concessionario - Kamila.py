class Concessionario():
    
    def __init__(self, tutte = 100, vendute = 0, offerta = 20):
        self.tutte_macchine = tutte
        self.macchine_vendute = vendute
        self.macchine_offerta = offerta 

    def storno(self):
        self.tutte_macchine = self.tutte_macchine - 1
        print("Stock macchine disponibili: ", self.tutte_macchine)

class Cars(Concessionario):
    def __init__(self, colore, tipo):
        self.colore_macchina = colore
        self.tipo_macchina = tipo 

class Marca(Cars):
    def __init__(self, colore, tipo, modello):
        Cars.__init__(self, colore, tipo)
        self.modello_macchina = modello

    def dati_macchina(self):
        print(self.tipo_macchina, self.modello_macchina, self.colore_macchina)

while True:

    print("-- Scegli un modello --")
    print("1. audi")
    print("2. bmw")
    print("3. mercedes")
    print("4. toyota")
    print("0. per uscire")

    scelta_modello = int(input("> "))

    print("-- Scegli un tipo --")
    print("C. coupe")
    print("D. decappottabile")
    print("U. utilitaria")
    print("V. van")
    
    scelta_tipo = input("> ")

    print("-- Scegli un colore --")
    print("R. rosso")
    print("B. bianco")
    print("N. nero")
    print("V. verde")
    print("A. azzurro")

    scelta_colore = input("> ")

    macchina = Marca(scelta_colore, scelta_tipo, scelta_modello)
    conteggio = Concessionario()

    if scelta_modello != False and scelta_colore != False and scelta_tipo != False:
        macchina.dati_macchina()
        conteggio.storno()

    elif scelta_modello == 0:
        break