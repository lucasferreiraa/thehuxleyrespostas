#68 - frigorífico

contador = 0
lista = []

while contador < quantidade:
	contador += 1
	ref, peso = map(float, input().split())
	lista.append(peso)

gordo = max(lista)
magro = min(lista)

print("Gordo: id: " + str(lista.index(max(lista))+1) + " peso: %.2f" % gordo + "Kg")
print("Magro: id: " + str(lista.index(min(lista))+1) + " peso: %.2f" % magro + "Kg")
