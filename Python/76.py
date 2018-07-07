#76 - correção das provas

import statistics

g = input()
gabarito = list(g)
nota = 0
lista = []

while True:
    entrada = input().split()
    matricula = int(entrada[0])
    if (matricula == 9999):
        break
    resposta = list(entrada[1])
    
    for i, j in zip(gabarito, resposta):
        if (i == j):
            nota += 1
    print(matricula, "%.1f" % nota)
    lista.append(nota)
    nota = 0
aux = 0
for i in lista:
    if (i >= 6):
        aux += 1
porcentagem = aux / (len(lista) / 100)
print(str("%.1f" % porcentagem) + "%")
print("%.1f" % statistics.mode(lista))