#87 - clones

while True:
    dicionario = {}
    qtd_dna, size_dna = map(int, input().split())
    
    if (qtd_dna == 0 and size_dna == 0):
        break
    
    for i in range(qtd_dna):
        dna = input().upper()
        if dna in dicionario:
            dicionario[dna] += 1
        else:
            dicionario[dna] = 0
    
    for j in range(qtd_dna) :
        contador = 0
        for k in dicionario.values():
            if (k == j):
                contador += 1
        print(contador)