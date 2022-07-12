# 8. Creare il sistema di classi Ospedale - Dottori - Specialisti. Far si chè ogni oggetto possa segnare le sue ore in una
#    lista separata e in una posizione univoca e che dall'oggetto ospedale si possa vedere il totale e pagare le ore (svuotare le liste)

class Ospedale: 
    lista_dottori = []
    lista_specialisti = []
    paga_dottori = []
    paga_specialisti = []
    def __init__(self, nome, cognome):
        self.n_medico = nome
        self.c_medico = cognome
    def nominativo(self):
        self.nom_cog = self.n_medico + " " + self.c_medico
        return self.nom_cog

class Dottori(Ospedale):
    def __init__(self, nome, cognome, prezzo=30):
        Ospedale.__init__(self, nome, cognome)
        self.euro_ora = prezzo

class Specialisti(Dottori):
    def __init__(self, nome, cognome, prezzo=50):
        Dottori.__init__(self, nome, cognome, prezzo=30)
        self.euro_ora = prezzo
        
def abbina_doc_ore(docs, euros):
    for i in range(len(docs)):
        for j in range(len(euros)):
            if i == j: 
                print(docs[i] + " - stipendio: " + str(euros[j]) + "€")

def fine_mese():
    Ospedale.lista_dottori = []
    Ospedale.lista_specialisti = []
    Ospedale.paga_dottori = []
    Ospedale.paga_specialisti = []

while True:
    print("-- Inizio mese --")
    i=0
    while True:    
        tipo = int(input("-- scegli: 0 per pagare a tutti, 1 per medico, 2 per specialista --  "))    
        
        if tipo == 0:
            break
        elif tipo == 1:    
            n_medico = input("Nome medico: ")
            c_medico = input("Cognome medico: ")
            medico = Dottori(n_medico, c_medico)
            ore_lavoro = int(input("Ore di lavoro da inserire: "))
            x = medico.nominativo()
            Ospedale.lista_dottori.append(x)
            Ospedale.paga_dottori.append(ore_lavoro*medico.euro_ora)
        elif tipo == 2:
            n_medico = input("Nome medico: ")
            c_medico = input("Cognome medico: ")
            medico_sp = Specialisti(n_medico, c_medico)
            ore_lavoro_sp = int(input("Ore di lavoro da inserire: "))
            y = medico_sp.nominativo()
            Ospedale.lista_specialisti.append(y)
            Ospedale.paga_specialisti.append(ore_lavoro_sp*medico_sp.euro_ora)
        else:
            print("Scelta non ammissibile")

        i+=1

    #controllo che mi riempie le liste  ---OK
    print("Dottori: ", Ospedale.lista_dottori)
    print("Ore Dottori: ",Ospedale.paga_dottori)
    print("Specialisti: ", Ospedale.lista_specialisti)
    print("Ore Specialisti: ", Ospedale.paga_specialisti)
    print()
    
    abbina_doc_ore(Ospedale.lista_dottori, Ospedale.paga_dottori)
    abbina_doc_ore(Ospedale.lista_specialisti, Ospedale.paga_specialisti)

    fine_mese()
    print()