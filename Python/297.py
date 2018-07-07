#297 - anos bissextos

ano_inicial, ano_final = map(int,input().split())

flag = True

for i in range(ano_inicial, ano_final+1):
    if (i % 400 == 0) or (i % 4 == 0 and i % 100 != 0):
        print(i)
        flag = False

if flag == True:
    print("-1")
