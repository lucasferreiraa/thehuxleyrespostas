#167 - eleições em Ambrolândia

alibaba = 83
alcapone = 93
vtsalibaba = []
vtsalcapone = []
brancos = []
nulos = []

while True:
	voto = int(input())
	if (voto == -1):
		break
	elif (voto == alibaba):
		vtsalibaba.append(voto)
	elif (voto == alcapone):
		vtsalcapone.append(voto)
	elif (voto == 0):
		brancos.append(voto)
	elif (voto != alibaba) or (voto != alcapone) or (voto != 0):
		nulos.append(voto)

print(len(vtsalibaba))
print(len(vtsalcapone))
print(len(brancos))
print(len(nulos))

if (len(vtsalibaba) > len(vtsalcapone)):
	print(alibaba)
else:
	print(alcapone)

validos = len(vtsalibaba) + len(vtsalcapone) + len(brancos)
porcentagem_alibaba = (len(vtsalibaba)*100.0) / validos
porcentagem_alcapone = (len(vtsalcapone)*100.0) / validos

print("%.2f" % porcentagem_alibaba)
print("%.2f" % porcentagem_alcapone)
