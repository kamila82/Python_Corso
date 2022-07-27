from asyncio.windows_events import NULL
import json 
import pickle

# 1. Creare una classe di due ereditarietà lineari che comunichino solo attraverso una classe in mezzo 

class Assicurazione():
    def __init__(self, ris_ass_rag = NULL):# -> None:
        self.risultato = ris_ass_rag
    
    def assegna_ragione(self):
        domn = "yes"
        while domn == "yes":
            domn = input("Vuoi vedere chi ha ragione? [yes/no] >> ")
            if domn != "yes":
                break
            else:
                valore = int(input("Passa valore danno: >>  "))
                if valore > 0:
                    self = Calcola_Ragione1()
                    self.risultato = "Ha ragione perito N° 1"
                    return self.risultato
                else: 
                    self = Calcola_Ragione2()
                    self.risultato = "Ha ragione perito N° 2"
                    return self.risultato

class Perito_1(Assicurazione):
    def __init__(self) -> None:
        super().__init__()

class Calcola_Ragione1(Perito_1):
    def __init__(self) -> None:
        super().__init__()

class Perito_2(Assicurazione):
    def __init__(self) -> None:
        super().__init__()
    
class Calcola_Ragione2(Perito_2):
    def __init__(self) -> None:
        super().__init__()

class Converting(Assicurazione):
    def __init__(self, ris_ass_rag):
        Assicurazione.__init__(self, ris_ass_rag)
        self.risultato = ris_ass_rag

    def conv_in_j(self):
        my_json = json.dumps(self.risultato)
        print("json", my_json, type(my_json))

    def conv_in_pickle(self):
        my_pickle = pickle.dumps(self.risultato)
        print("pickle", my_pickle, type(my_pickle))

while True:
    assic = Assicurazione()
    x = assic.assegna_ragione()
    print(x)
    scelta = input("J - converti to json \nP - converti to pickle  \n>>  ")
    conv = Converting(x)

    if scelta == "J":
        conv.conv_in_j()
    else:
        conv.conv_in_pickle()
