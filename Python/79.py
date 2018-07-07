#79 - multiplicação da diagonal de uma matriz

entrada = int(input())
matriz = []

while entrada != 0:
    for i in range(4):
        a = []
        for i in range(4):
            b = int(input())
            a.append(b)
        matriz.append(a)
    
    for i in range(4):
        matriz[i][i] *= entrada
    
    for i in range(4):
        for j in range(4):
            print(matriz[j][i], end = " ")
        print()
    matriz = []
    entrada = int(input())