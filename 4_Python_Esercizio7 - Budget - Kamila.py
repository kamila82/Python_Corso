from asyncio.windows_events import NULL
import random

# 7. Utilizzare il seguente schema (Comune - due classi figli: Asl, Proloco)
#   Creare un sistema di suddivisione del budget in entrata 

class Comune:
    def __init__(self, budget_totale): 
        self.budget_tot = budget_totale
        self.bud_Asl = self.budget_tot * 0.3
        self.bud_Pro = self.budget_tot * 0.25
    
    def dati_budget_tot(self):
        print("Budget Comune: ", self.budget_tot, "Budget Asl: ", self.bud_Asl, "Budget Proloco: ", self.bud_Pro, "\n")

class Asl(Comune):
    def __init__(self):
        self.bud_Asl = 0

class Proloco(Comune):
    def __init__(self):
        self.bud_Pro = 0

while True:
    input_budget = int(input("Inserisci budget totale: "))
    budget = Comune(input_budget)
    budget.dati_budget_tot()

