   
#2. Crea un sistema di if e classi (AziendaMadre --> Sussidiaria) che permetta di inserire valori in entrata e che calcoli 
# in base al figlio (ne dovrà avere almeno 2) le tasse che dovrà pagare rispetto al numero inserito. Dev'essere ripetibile 

class AziendaMadre:
    def __init__(self, fatturato): 
        self.invoiced = fatturato

class Sussidiaria_1(AziendaMadre):
    def __init__(self, fatturato, tasse):
        AziendaMadre.__init__(self, fatturato)
        self.tax = tasse
    def dati_tax(self):
        print("Tasse:", self.invoiced * self.tax)    

class Sussidiaria_2(AziendaMadre):
    def __init__(self, fatturato, tasse):
        AziendaMadre.__init__(self, fatturato)
        self.tax = tasse
    def dati_tax(self):
        print("Tasse:", self.invoiced * self.tax)

while True:
    print(" -- Benvenuti nella Climbing Technology -- ")

    invoiced = int(input("Valore fatturato >>   "))
    
    ct = AziendaMadre(invoiced)

    visualizza = input("Tasse pagate dove vuoi vedere: 1 o 2 >> " )
    if visualizza == "1":
        ct_sede_1 = Sussidiaria_1(invoiced, 0.3)
        ct_sede_1.dati_tax()
    else:
        ct_sede_2 = Sussidiaria_1(invoiced, 0.4)
        ct_sede_2.dati_tax()
    print()
