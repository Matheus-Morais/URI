x, y, = input().split()
x = float(x)
y = float(y)
if x == y == 0:
    mensagem = 'Origem'
elif x == 0 and y != 0:
    mensagem = 'Eixo Y'
elif x != 0 and y == 0:
    mensagem = 'Eixo X'
elif x > 0 and y > 0:
    mensagem = 'Q1'
elif x < 0 and y > 0:
    mensagem = 'Q2'
elif x < 0 and y < 0:
    mensagem = 'Q3'
else:
    mensagem = 'Q4'
print(mensagem)