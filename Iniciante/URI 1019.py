tempoTotal = int(input())
horas = tempoTotal // 3600
minutos = (tempoTotal - horas*3600) // 60
segundos = tempoTotal - horas*3600 - minutos*60
print(f'{horas}:{minutos}:{segundos}')