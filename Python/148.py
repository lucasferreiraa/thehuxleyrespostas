#148 - buracos no texto

casos = int(input())
contador = 0
while contador < casos:
    contador += 1
    palavra = input()
    palavra = palavra.upper()
    buraco = 0

    for i in palavra:
        if (i == "A") or (i == "D") or (i == "O") or (i == "P") or (i == "R") or (i == "Q"):
            buraco += 1
        elif (i == "B"):
            buraco += 2
        else:
            pass
    
    print(buraco)
    buraco = 0