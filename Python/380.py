#380 - escolhendo o passeio

cinema = 0
boliche = 0
contador = 0

while contador < 7:
	opcao = input()
	opcao = opcao.upper()
	if (opcao == 'CINEMA'):
		cinema = cinema + 1
	elif (opcao == 'BOLICHE'):
		boliche = boliche + 1
	contador = contador + 1

if (cinema > boliche):
	print("CINEMA")
else:
	print("BOLICHE")
