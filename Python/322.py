#322 - menor valoe e posição

n = int(input())
entrada = input().split()

lista = []

for i in entrada:
	a = int(i)
	lista.append(a)

if (len(lista) == n):
	print("Menor valor:", min(lista))
	print("Posicao:", lista.index(min(lista)))
else:
	print("Programa finalizado")
