# 9. Crea una classe Fabbrica che deriva 3 classi figlie che non hanno attributi ne metodi oltre a un print 
#    per descriversi e un init e vongono costruite della classe padre quindi far si che istanziando il padre 
#    si possa creare uno dei tre oggetti

class Fabbrica:
    def __init__(self, nome_fabbrica):
        self.nome = nome_fabbrica

    def crea_reparti(self):

        moschettoni = Moschettoni(self.nome)
        imbraghi = Imbraghi(self.nome)
        caschi = Caschi(self.nome)
        print()

        scelta = int(input("Cerca mail del reparto: 1. per Moschettoni 2. per Imbraghi 3. per Caschi   "))
        i=0
        while i<1:
            if scelta == 0:
                break
            elif scelta == 1:
                moschettoni.__init__(self.nome)
            elif scelta == 2:
                imbraghi.__init__(self.nome)
            elif scelta == 3:
                caschi.__init__(self.nome)
            i+=1
        
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

fabbrica = Fabbrica("ClimbingTechnology")
fabbrica.crea_reparti()
