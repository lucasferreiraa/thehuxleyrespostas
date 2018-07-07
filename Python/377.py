#377 - líder do grupo da copa

time1 = input()
pontos1 = int(input())
saldo1 = int(input())
golspro1 = int(input())
time2 = input()
pontos2 = int(input())
saldo2 = int(input())
golspro2 = int(input())

if (pontos1 > pontos2) or (pontos1 == pontos2 and saldo1 > saldo2) or (pontos1 == pontos2 and saldo1 == saldo2 and golspro1 > golspro2):
	print(time1.lower())
elif (pontos1 < pontos2) or (pontos1 == pontos2 and saldo1 < saldo2) or (pontos1 == pontos2 and saldo1 == saldo2 and golspro1 < golspro2):
	print(time2.lower())
else:
	print ("EMPATE")
