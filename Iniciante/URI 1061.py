diaInicio = input('Dia:').split()
horaI, minutoI, segundoI = input().split(':')
diaFim = input('Dia:').split()
horaF, minutoF, segundoF = input().split(':')
diaInicio = int(diaInicio)
diaFim = int(diaFim)
horaI = int(horaI)
minutoI = int(minutoI)
segundoI = int(segundoI)
horaF = int(horaF)
minutoF = int(minutoF)
segundoF = int(segundoF)

diaTotal = diaFim - diaInicio
horaTotal = horaF - horaI
minutoTotal = minutoF - minutoI
segundoTotal = segundoF - segundoI

if horaTotal < 0:
    horaTotal += 24
    diaTotal -= 1
if minutoTotal < 0:
    minutoTotal += 60
    horaTotal -= 1
if segundoTotal < 0:
    segundoTotal += 60
    minutoTotal -= 1

print(f"{diaTotal} dia(s)")
print(f"{horaTotal} hora(s)")
print(f"{minutoTotal} minuto(s)")
print(f"{segundoTotal} segundo(s)")