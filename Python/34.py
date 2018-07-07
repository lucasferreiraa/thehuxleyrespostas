#34 - saque de banco

valor = int(input())

cinquenta = valor // 50
valor = valor % 50

vinte = valor // 20
valor = valor % 20

dez = valor // 10
valor = valor % 10

cinco = valor // 5
valor = valor % 5

um = valor // 1

print("Notas de 50:", cinquenta)
print("Notas de 20:", vinte)
print("Notas de 10:", dez)
print("Notas de 5:", cinco)
print("Notas de 1:", um)