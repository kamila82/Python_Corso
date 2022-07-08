class Scuola():
    def __init__(self, nome, cognome):
        self.tuonome = nome
        self.tuocognome = cognome

class Studente(Scuola):
    lista_studenti_1 = []
    def __init__(self, nome, cognome, eta, matricola):
        Scuola.__init__(self, nome, cognome)
        self.etastudente = eta
        self.numero_matricola = matricola
        self.settalista()

    def dati_studente(self):
        print(self.tuonome, self.tuocognome, self.etastudente, self.numero_matricola)

    def settalista(self):
        self.lista_studenti_1.append(self.tuonome)

class Docente(Scuola):
    lista_docenti_1 =[]
    def __init__(self, nome, cognome, profilo):
        Scuola.__init__(self, nome, cognome)
        self.profilo_classe = profilo
        self.settalista()

    def dati_docente(self):
        print(self.tuonome, self.tuocognome, self.profilo_classe)

    def settalista(self):
        self.lista_docenti_1.append(self.tuonome)

lista_di_tutti = []

while True:

    lista_studenti =[]
    lista_docenti =[]

    print("-- SELEZIONARE TIPO UTENTE --")
    print("1. studente")
    print("2. docente")
    print("0. per uscire")

    persona = int(input("> "))

    if persona == 1:
        print("Sezione Studenti")
        x = input("Nome: ")
        y = input("Cognome: ")
        z = input("Eta: ")
        a = input("Matricola: ")
        studente = Studente(x, y, z, a)
        studente.dati_studente()
        lista_studenti.append(studente.tuonome)
        lista_studenti.append(studente.tuocognome)
        lista_studenti.append(studente.etastudente)
        lista_studenti.append(studente.numero_matricola)

        lista_di_tutti.append(lista_studenti)

    elif persona == 2: 
        print("Sezione Docenti")
        x = input("Nome: ")
        y = input("Cognome: ")
        z = input("Profilo: ")  
        docente = Docente(x, y, z)
        docente.dati_docente()
        lista_docenti.append(docente.tuonome)
        lista_docenti.append(docente.tuocognome)
        lista_docenti.append(docente.profilo_classe)
    
        lista_di_tutti.append(lista_docenti)

    elif persona == 0:
        print(lista_di_tutti)
        break

print()
print("Studenti: ", len(Studente.lista_studenti_1),Studente.lista_studenti_1) 
print("Docenti: ", len(Docente.lista_docenti_1), Docente.lista_docenti_1)