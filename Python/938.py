# 938 - 5 valores para a

lista = []
negativos = []
contador = 0

while (contador < 5):
    entrada = float(input())
    lista.append(entrada)
    contador += 1

for i in lista:
    if (i < 0):
        negativos.append(i)
    else:
        pass
    
negativo = len(negativos)
print("Digite um valor:")
print("Digite um valor:")
print("Digite um valor:")
print("Digite um valor:")
print("Digite um valor:")
print("Foram digitados " + str(negativo) + " numeros negativos")
