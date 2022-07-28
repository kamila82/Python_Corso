#from Coverter_Kamila import *
from asyncio.windows_events import NULL

# 1. Utilizza una classe eredita lineare all interno di una gerachia per generare un dict di dati (nome, cognome, password) 
#    che deve essere conervato nel figlio 1-2 ma modificato dalle classi parallele.
#    Le modifiche saranno: cambia parametri , elimina account, crea nuovo account 
#    dorvà essere ripetibile e stampare la lista di dic presenti 

class Menu_principale:
    def __init__(self) -> None: 
        pass
    # def __init__(self, utente): 
    #     self.ut = utente

    def scelta_menu(self):
        while True: 
            scelta = input("1. Visualizza \n2. Modifica \n0. Esci dal programma\n>>  ")
            if scelta == "0":
                print("FINE")
                break
            elif scelta == "1":
                print("Visualizzazione utenti: ", end="")
                vis = Figlio()
            elif scelta == "2": 
                print("Modifica\n")
                modif = Modificatore()
                modif.modifica_account()                
            else:
                print("Scelta non consentita\n")

class Figlio(Menu_principale):
    def __init__(self) -> None: 
        self.visualizza()

    def visualizza(self):
        if lista_utenti == {}:
            print("Nessun utente da visualizzare\n")
        else:
            print(lista_utenti)

class Modificatore():
    def __init__(self, utente=NULL): 
        self.ut = utente

    def modifica_account(self):
        domn = "C"
        while domn == "C" or domn == "E" or domn == "A":
            domn = input("C. Cambia account\nE. Elimina account\nA. Aggiungi account \n0. Menu precedente \n>> ")
            if domn == "0":
                break
            elif domn != "C" and domn != "E" and domn != "A" and domn != "0":
                print("Scelta non consentita")
                print()
            else:
                if domn == "C":
                    self = Cambia(self.ut)
                elif domn == "E":
                    self = Elimina(self.ut)
                elif domn == "A":
                    self = Aggiungi(self.ut)

class Cambia(Modificatore):
    def __init__(self, utente):
        Modificatore.__init__(self, utente)
        self.cambia_acount()
    def cambia_acount(self):
        print(lista_utenti)
        numero_utente = int(input("Numero utente da cambiare >> " ))
        print(lista_utenti[numero_utente])
        ut_da_mod = lista_utenti[numero_utente]
        scelta_modifica = input("Quale campo vuoi aggiornare >> " )
        nuovo_dato = input("Inserisci nuovo dato >> ")
        ut_da_mod[scelta_modifica]=nuovo_dato
        print(lista_utenti)

class Elimina(Modificatore):
    def __init__(self, utente):
        Modificatore.__init__(self, utente)
        self.elimina_account()

    def elimina_account(self):
        print(lista_utenti)
        numero_utente = int(input("Numero utente da eliminare: >>" ))
        lista_utenti.pop(numero_utente)
        print(lista_utenti)

class Aggiungi(Modificatore):
    def __init__(self, utente):
        Modificatore.__init__(self, utente)
        self = aggiungi_account()

def aggiungi_account():        
        num = int(input("Numero utente >> " ))
        nome = input("Nome utente >> " )
        cognome = input("Cognome utente >> " )
        data = input("Data creazione account >> " )
        passw = input("Password >> " )
        ut = {"nome":nome, "cognome": cognome, "data":data, "password": passw} 
        lista_utenti[num] = ut
        print(lista_utenti)
        print()

lista_utenti= {}
prima_scelta = Menu_principale()
prima_scelta.scelta_menu()
