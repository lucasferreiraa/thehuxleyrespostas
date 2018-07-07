#933 - próximos da média

quantidade = int(input())
lista = []
lista2 = []
soma_notas = 0

for i in range(quantidade):
	notas = float(input())
	soma_notas += notas
	lista.append(notas)

media = soma_notas / quantidade  

for i in range(len(lista)):
	x = media - lista[i]
	x = abs(x)
	lista2.append(x)

x = min(lista2)
y = lista2.index(x)
z = lista[y]

print('MEDIA: %.2f' % media)
print('MAIS PROXIMO: %.2f' % z)
print('DIFERENCA: %.2f' % x)