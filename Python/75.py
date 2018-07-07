#75 - reserva de passagens

voo = {}

for i in range(37):
    entrada = input().split()
    voo[entrada[0]] = int(entrada[1])
entrada = input().split()

while entrada[0] != '9999':
    if entrada[1] in voo.keys():
        if voo[entrada[1]] > 0:
            print(entrada[0])
            voo[entrada[1]] -= 1
        else:
            print('INDISPONIVEL')
    else:
        print('INDISPONIVEL')
    entrada = input().split()