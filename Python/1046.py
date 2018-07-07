#1046 - capacidade canal de transmissão

video = float(input())
audio = float(input())
dados = float(input())
capacidade = float(input())

result = (video*5.2 + audio*3.4 + dados*1.5) / capacidade

print("%.2f" % round(result, 2))
