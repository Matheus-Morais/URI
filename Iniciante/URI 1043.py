x, y, z = input().split()
x = float(x)
y = float(y)
z = float(z)
if ((abs(y - z)) < x < (y + z)) and ((abs(x - z)) < y < (x + z)) and ((abs(x - y)) < z < (x + y)):
    calculo = x + y + z
    texto = 'Perimetro'
else:
    calculo = ((x + y) * z) / 2
    texto = 'Area'
print(f'{texto} = {calculo:.1f}')