#841 - acima da média

cont = 0
lista = []
while cont < 3:
    cont += 1
    num = float(input())
    lista.append(num)
media = sum(lista) / cont
acima = 0
for i in lista:
    if (i > media):
        acima += 1
print(acima)