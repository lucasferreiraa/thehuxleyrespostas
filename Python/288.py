#288 - apresentação do trabalho

ig, ia, encaps, indent, stru = map(int, input().split())

if (ig == 1 or ia == 1) and (encaps == 1 and indent == 1) and stru == 1:
    print("AVALIADO")
else:
    print(0)
