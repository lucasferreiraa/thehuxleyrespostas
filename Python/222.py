#222 - campeonato

cv, ce, cs, fv, fe, fs = map(int, input().split())

pontos_c = (cv*3) + ce
pontos_f = (fv*3) + fe

if (pontos_c > pontos_f):
    print("C")
elif (pontos_c < pontos_f):
    print("F")
elif (pontos_c == pontos_f) and (cs > fs):
    print("C")
elif (pontos_c == pontos_f) and (cs < fs):
    print("F")
else:
    print("=")
