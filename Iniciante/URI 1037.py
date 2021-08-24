numero = float(input())
if 0 <= numero <= 25:
    mensagem = 'Intervalo [0,25]'
elif 25 < numero <= 50:
    mensagem = 'Intervalo (25,50]'
elif 50 < numero <= 75:
    mensagem = 'Intervalo (50,75]'
elif 75 < numero <= 100:
    mensagem = 'Intervalo (75,100]'
else:
    mensagem = 'Fora de intervalo'
print(mensagem)