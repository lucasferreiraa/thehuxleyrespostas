#1086 - aluguel de carro

dias = int(input())
kilometros = int(input())

valor_dias = dias * 30.0
valor_km = kilometros * 0.01

desc = (valor_dias + valor_km) * 0.10
total = (valor_dias + valor_km) - desc

print("%.2f" % total)
