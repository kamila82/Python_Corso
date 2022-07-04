# class Primaclasse():
#     x = 1
#     y = 1.75
#     b = True
#     m = "mirko"

#---------------------DOMANDA 1------------------------------------------------------
x = input("Dammi un input.... ")
if(x!=False):
    print(x)
    
#---------------------DOMANDA 2------------------------------------------------------
nome = input("Come ti chiami? ")
if(nome!=False): 
    print(nome)

eta = int(input("Quanti anni hai? "))
if(eta>0 and eta <120): 
    print(eta)

citta = input("Dove vivi? ")
if(citta!=False): 
    print(citta)
    
#---------------------DOMANDA 3-----------------------------------------------------
lista = []

nome = input("Come ti chiami? ")
if(nome!=False):
    lista.append(nome)
    print(lista)

eta = int(input("Quanti anni hai? "))

if(eta>0 and eta <120): 
    lista.append(eta)
    print(lista)

citta = input("Dove vivi? ")
if(citta!=False):
    lista.append(citta)
    print(lista)