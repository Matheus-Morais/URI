inicio, fim = input().split()
inicio = int(inicio)
fim = int(fim)
if inicio < fim:
    tempoTotal = fim - inicio
else:
    tempoTotal = (24 - inicio) + fim
print(f'O JOGO DUROU {tempoTotal} HORA(S)')