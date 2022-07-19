import json
import pickle
    
#2. Crea un sistema di if e classi (AziendaMadre --> Sussidiaria) che permetta di inserire valori in entrata e che calcoli 
# in base al figlio (ne dovrà avere almeno 2) le tasse che dovrà pagare rispetto al numero inserito. Dev'essere ripetibile 

# class AziendaMadre:
#     def __init__(self, fatturato): 
#         self.invoiced = fatturato

# class Sussidiaria_1(AziendaMadre):
#     def __init__(self, fatturato, tasse):
#         AziendaMadre.__init__(self, fatturato)
#         self.tax = tasse
#     def dati_tax(self):
#         print("Tasse:", self.invoiced * self.tax)    

# class Sussidiaria_2(AziendaMadre):
#     def __init__(self, fatturato, tasse):
#         AziendaMadre.__init__(self, fatturato)
#         self.tax = tasse
#     def dati_tax(self):
#         print("Tasse:", self.invoiced * self.tax)

# while True:
#     print(" -- Benvenuti nella Climbing Technology -- ")

#     invoiced = int(input("Valore fatturato >>   "))
    
#     ct = AziendaMadre(invoiced)

#     visualizza = input("Tasse pagate dove vuoi vedere: 1 o 2 >> " )
#     if visualizza == "1":
#         ct_sede_1 = Sussidiaria_1(invoiced, 0.3)
#         ct_sede_1.dati_tax()
#     else:
#         ct_sede_2 = Sussidiaria_1(invoiced, 0.4)
#         ct_sede_2.dati_tax()
#     print()

#3. Crea un sistema che dati in input 3 dati in una lista la possa convertire in json e pickle e che sia ripetibile
# sfruttando l'incapsulamento delle classi per lavorare avendo solo i metodi del figlio richiamati dal padre

class Sistema:
    def __init__(self) -> None: 
       pass

class Converter_1(Sistema):
    def __init__(self) -> None:
        super().__init__()
    def salva_dati(self):
        in_json = json.dumps(lista)
        print(in_json, type(in_json))
        return(in_json)

class Converter_2(Sistema):
    def __init__(self) -> None:
        super().__init__()
    def salva_dati(self):
        in_pickle = pickle.dumps(lista)
        print(in_pickle, type(in_pickle))
        return(in_pickle)


while True: 
    lista = []
    domanda = int(input("Vuoi 1 - procedere alla nuova sessione 0 - interrompere >> "))
    if domanda == 0:
        break
    else:
        print("tua lista: ", lista)
        i = 0
        while i < 3: 
            x = int(input("Aggiungi un valore alla lista >> "))
            lista.append(x)
            i += 1
        print(lista, type(lista))

        scelta = input("J - converti in json, P - converti in pickle  >>  ")
        if scelta == "J":
            conv1 = Converter_1()
            in_json = conv1.salva_dati()        
            riconv_J_to_py = input("Vuoi riconvertire? >>  ")
            if riconv_J_to_py == "si":
                lista = json.loads(in_json)
                print(lista, type(lista))
        if scelta == "P":
            conv2 = Converter_2()
            in_pickle = conv2.salva_dati()
            riconv_P_to_py = input("Vuoi riconvertire? >>  ")
            if riconv_P_to_py == "si":
                lista = pickle.loads(in_pickle)
                print(lista, type(lista))
        print()
