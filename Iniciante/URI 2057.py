horaSaida, tempoViagem, fuso = input().split()
horaSaida = int(horaSaida)
tempoViagem = int(tempoViagem)
fuso = int(fuso)
calculo = horaSaida + tempoViagem + fuso
if calculo < 0:
    horaPrevista = 24 + calculo
elif 0 <= calculo < 24:
    horaPrevista = calculo
elif calculo >= 24:
    horaPrevista = calculo - 24
print(horaPrevista)