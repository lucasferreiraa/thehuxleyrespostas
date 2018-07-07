#763 - tamanho do palíndromo

palavra = input()

if (palavra == palavra[::-1]):
    print("SIM")
    if (len(palavra) % 2 == 0):
        print(len(palavra) // 2)
    else:
        print((len(palavra) // 2) + 1)
else:
    print("NAO")