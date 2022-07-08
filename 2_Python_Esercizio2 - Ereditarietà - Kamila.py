class Anagrafica():
    dati_personali =[]
    nome = "x"
    cognome = "y"
    eta = 1
    lavoro = "z"
    
utente = Anagrafica()

utente.nome = input("Tuo nome: ")
if(type(utente.nome)==str):
#    print(utente.nome)
    utente.dati_personali.append(utente.nome)

utente.cognome = input("Tuo cognome: ")
if(type(utente.cognome)==str):
#    print(utente.cognome)
    utente.dati_personali.append(utente.cognome)

utente.eta = input("Tua eta: ")
if(type(int(utente.eta))==int):
#    print(utente.eta)
    utente.dati_personali.append(utente.eta)

utente.lavoro = input("Tuo lavoro: ")
if(type(utente.lavoro)==str):
#    print(utente.lavoro)
    utente.dati_personali.append(utente.lavoro)

print(utente.dati_personali)
#------------------------------------------------------------

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname)

x = Person("John", "Doe")
x.printname()
