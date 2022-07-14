# 9. Crea una classe Fabbrica che deriva 3 classi figlie che non hanno attributi ne metodi oltre a un print
#    per descriversi e un init e vongono costruite della classe padre quindi far si che istanziando il padre
#    si possa creare uno dei tre oggetti

class Fabbrica:
    def __init__(self, nome_fabbrica):
        self.nome = nome_fabbrica

    def crea_rep_moschettoni(self):
        moschettoni = Moschettoni(self.nome)

    def crea_rep_imbraghi(self):
        imbraghi = Imbraghi(self.nome)

    def crea_rep_caschi(self):
        caschi = Caschi(self.nome)

class Moschettoni(Fabbrica):
    def __init__(self, nome_fabbrica):
        Fabbrica.__init__(self, nome_fabbrica)
        print("moschettoni@"+self.nome+".it")

class Imbraghi(Fabbrica):
    def __init__(self, nome_fabbrica):
        Fabbrica.__init__(self, nome_fabbrica)
        print("imbraghi@"+self.nome+".it")

class Caschi(Fabbrica):
    def __init__(self, nome_fabbrica):
        Fabbrica.__init__(self, nome_fabbrica)
        print("caschi@"+self.nome+".it")

while True:
    scelta = int(input("Cerca mail del reparto: \nemmetti 1. per Moschettoni 2. per Imbraghi 3. per Caschi 0. per uscire >> "))
    fabbrica = Fabbrica("ClimbingTechnology")
    if scelta == 0:
        break
    elif scelta == 1:
        fabbrica.crea_rep_moschettoni()
    elif scelta == 2:
        fabbrica.crea_rep_imbraghi()
    elif scelta == 3:
        fabbrica.crea_rep_caschi()
    print()