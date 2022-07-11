from asyncio.windows_events import NULL

class Zoo():
    recinto_1 = []
    recinto_2 = []
    recinto_3 = []

    def __init__(self, nome):
        self.nome_animale = nome

class Animale(Zoo):
    def __init__(self, nome, cosa_fa=NULL):
        Zoo.__init__(self, nome)
        self.tipo_animale = cosa_fa
    
    def dati_recinti(self):
        print("Recinto 1 contiene:", self.recinto_1, "Recinto 2 contiene: ", self.recinto_2, "Recinto 3 contiene: ", self.recinto_3)

    def controlla_ripetizioni(self):
        if self.nome_animale not in Zoo.recinto_1 and self.nome_animale not in Zoo.recinto_2 and not self.nome_animale in Zoo.recinto_3:
            return True
        else: 
            print("Animale già in recinto")

def cosa_fa(cosa_fa):
    if cosa_fa == 1:
        Zoo.recinto_1.append(nome_animale)
    elif cosa_fa == 2:
        Zoo.recinto_2.append(nome_animale)
    else:
        Zoo.recinto_3.append(nome_animale)

i = 1
while i!=7:
    lista_animali = {1:"balena", 2:"leone", 3:"gazella", 4:"squalo", 5:"delfino", 6:"airone", 7:"pappagallo", 8:"piccione", 9:"tigre"}
    print(lista_animali)
    numero_animale = int(input("Che animale sei? Scegli un numero: "))
    nome_animale = lista_animali[numero_animale]
    animale = Animale(nome_animale)

    if animale.controlla_ripetizioni() == True:
        print("Cosa sai fare?")
        print("1. volare")
        print("2. nuotare")
        print("3. nessuno dei precedenti")
        
        cosa_sai_fare = int(input(">> "))
        cosa_fa(cosa_sai_fare)
        animale = Animale(nome_animale, cosa_sai_fare)
    else:
        continue
    
    i+=1

Animale.dati_recinti(animale)