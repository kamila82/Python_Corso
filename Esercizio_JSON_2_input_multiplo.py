import json #una libreria

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
