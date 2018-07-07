#166 - algarismo da casa das unidades

numero = int(input()) 

algarismo = numero % 10

if (numero < 0): 
    algarismo += -10
     
print(algarismo)
