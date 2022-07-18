import json #una libreria

# RICEVERE UN JSON
x = '{"Nome": "Mirko", "Eta":"36", "Citta": "New York"}'

y = json.loads(x) #carichiamo nell'elemento y i dati di x
#print(y)
#print(y["Eta"]) #una stringa che va stampata come un dizionario
#print()

# INVIARE e CREARE UN JSON
x1 = {
    "Nome": "Mirko", 
    "Eta":"36", 
    "Citta": "New York"
    }

y1 = json.dumps(x1) #carichiamo nell'elemento y i dati di x
#print(y1) #un dizionario che va convertito in una stringa 

#json.dumps(y1, indent=4)
#json.dumps(y, indent=4, separators=(". ", ": "))
#json.dumps(y, indent=4, sort_keys=True) #può ordinare automaticamente un elemento 
#print(y1)

# ESERCIZIO - creare una struttra di input che permetta di accedere a due sistemi:
# 1) prenderà i dati in entrata e scriverà (dumps) un file di JSON salvando in una mia_lista
# 2) prenderà tra una mia_lista un input e caricherà un file JSON
# 3) il sistema dovrà aspettare l'END  per terminare e dovrà prima farti caricare almeno un dato 

mia_lista = []

while True:
    loop_1 = input("1. Inserire i dati 2. Caricare i dati 0. Uscire >>   ")
    if loop_1 == "0":
        break
    elif loop_1 == "1":
        loop_2 = "si"
        while loop_2 == "si":
            input_utente = input("Nome/Cognome da inserire >>   ")
            mia_lista.append(input_utente)
            stringa = json.dumps(mia_lista)
            print(stringa)
            loop_2 = input("Vuoi inserire un elemento? >>   ")
    else:
        stringa = json.dumps(mia_lista)
        print(stringa)
        loop_3 = "si"
        y = json.loads(stringa)
        while loop_3 == "si":
            vis_elem = int(input("Quale elemento vuoi visualizzare? >>   "))
            if stringa != []:    
                print(y[vis_elem])
                loop_3 = input("Vuoi visualizzare un elemento?  ")
            elif stringa == []:
                print("Non c'è ancora nulla da visualizzare")
print(mia_lista)