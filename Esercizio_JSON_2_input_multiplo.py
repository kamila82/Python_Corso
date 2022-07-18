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
# 1) prenderà i dati in entrata e scriverà (dumps) un file di JSON salvando in una mio_elenco
# 2) prenderà tra una mio_elenco un input e caricherà un file JSON
# 3) il sistema dovrà aspettare l'END  per terminare e dovrà prima farti caricare almeno un dato 

mio_elenco = {}
x = 1

while True:
    loop_1 = input("1. Inserire i dati 2. Caricare i dati 0. Uscire >>   ")
    if loop_1 == "0":
        break
    elif loop_1 == "1":
        loop_2 = "si"
        while loop_2 == "si":
            domanda = input("Vuoi inserire: '1' per uno, '+' per più untenti, '0' per uscire >>   ")
            if domanda == "1":
                input_utente = input("Nome >>   ")  
                mio_elenco[(x)]=input_utente
                stringa = json.dumps(mio_elenco)
                print(stringa)
                x += 1
            elif domanda == "+":
                quanti = int(input("Quanti nomi vuoi aggiungere? >> "))
                lista_nomi = []
                for i in range (quanti):
                    input_utente = input("Nome >>   ")
                    mio_elenco[(x)]=input_utente
                    elenco_stringa = json.dumps(mio_elenco)
                    print(elenco_stringa)
                    x += 1
            elif domanda == "0":
                break
    else:
        elenco_stringa = json.dumps(mio_elenco)
        print(elenco_stringa)
        #print(len(elenco_stringa))
        y = json.loads(elenco_stringa)
        loop_3 = "si"
        while loop_3 == "si":
            #if len(elenco_stringa) > 2:    #potrei anche estrarre tutte le chiavi dal dict e poi contarle (len)
            if len(mio_elenco.keys()) > 0:
                vis_elem = input("Quale elemento vuoi visualizzare? >>   ")
                print(y[vis_elem])
                loop_3 = input("Vuoi visualizzare un elemento?  ")
            else:
                print("Non c'è ancora nulla da visualizzare")
                break
print(mio_elenco)