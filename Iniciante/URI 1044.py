x, y = input().split()
x = int(x)
y = int(y)
if (x % y) == 0 or (y % x) == 0:
    texto = 'Sao'
else:
    texto = 'Nao sao'
print(f'{texto} Multiplos')