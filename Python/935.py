#s935 - aprovação

nota1 = float(input())
nota2 = float(input())
nota3 = float(input())

media = (nota1 + nota2 + nota3) / 3

if (media >= 7):
    print("Informe a primeira nota:")
    print("Informe a segunda nota:")
    print("Informe a terceira nota:")
    print("Aprovado com media", media)
elif (media >= 5 and media < 7):
    print("Informe a primeira nota:")
    print("Informe a segunda nota:")
    print("Informe a terceira nota:")
    print("Recuperacao com media", media)
else:
    print("Informe a primeira nota:")
    print("Informe a segunda nota:")
    print("Informe a terceira nota:")
    print("Reprovado com media", media)
