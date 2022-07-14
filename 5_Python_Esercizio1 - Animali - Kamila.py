from asyncio.windows_events import NULL

# 1. Crea una classe Animali che deriva 3 classi figlie che non ha ogni uno un suo attributo
#    i figli vengono costruiti della classe padre dopo l'inserimento via input e la tipo del tipo di oggetto da creare

class Animali:
    def __init__(self,tipo_a, nome_a):
        self.tipo =tipo_a
        self.nome = nome_a

    def crea_Felino(self):#,tipo_a, nome_a):
        self.vel = 60
        print(self.nome,"velocita",self.vel, "km/h")

    def crea_Canide(self):
        self.zam = 4
        print(self.nome,"ha",self.zam, "zampe")

    def crea_Uccello(self):
        self.col = "grigio"  
        print(self.nome,"è di colore", self.col)

class Felino(Animali):
    def __init__(self,tipo_a, nome_a, velocita):
        Animali.__init__(self,tipo_a, nome_a)
        self.vel = velocita
    
class Canide(Animali):
    def __init__(self,tipo_a, nome_a, zampe):
        Animali.__init__(self,tipo_a, nome_a)
        self.zam = zampe 

class Uccello(Animali):
    def __init__(self,tipo_a, nome_a, colore):
        Animali.__init__(self,tipo_a, nome_a)
        self.col = colore

while True:
    nome = input("Nome animale >> ")
    tipo = int(input("Tipo di animale >> 1. per Felino 2. per Canide 3. per Uccello 0. per uscire >> "))
    animale = Animali(tipo, nome)

    if tipo == 0:
        break
    elif tipo == 1:  
        animale.crea_Felino()
    elif tipo == 2:
        animale.crea_Canide()
    elif tipo == 3:
        animale.crea_Uccello()
    print()

