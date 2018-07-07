# 691 - 2 números em ordem crescente

a, b = map(int, input().split())

if (a < b):
    print(a, b)
elif (a > b):
    print(b, a)
else:
    print(a, b)
