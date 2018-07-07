#289 - brinquedos do parque

altura, idade = map(int, input().split())
cont = 0
if (altura >= 150 and idade >= 12):
    cont += 1
if (altura >= 140 and idade >= 14):
    cont += 1
if (altura >= 170 or idade >= 16):
    cont += 1
print(cont)
