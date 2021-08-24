x, y, z = input().split()
x = float(x)
y = float(y)
z = float(z)
if x >= y and x >= z:
    maior = x
    if y >= z:
        meio = y
        menor = z
    else:
        meio = z
        menor = y
elif y >= x and y >= z:
    maior = y
    if x >= z:
        meio = x
        menor = z
    else:
        meio = z
        menor = x
elif z >= x and z >= y:
    maior = z
    if x >= y:
        meio = x
        menor = y
    else:
        meio = y
        menor = x
elif x == y and y == z:
    maior=x
    meio=y
    menor=z

if maior >= (meio + menor):
    print('NAO FORMA TRIANGULO')
else:
    if (maior ** 2) == (meio ** 2 + menor ** 2):
        print('TRIANGULO RETANGULO')
    if (maior ** 2) > (meio ** 2 + menor ** 2):
        print('TRIANGULO OBTUSANGULO')
    if (maior ** 2) < (meio ** 2 + menor ** 2):
        print('TRIANGULO ACUTANGULO')
    if maior == meio == menor:
        print('TRIANGULO EQUILATERO')
    if maior == meio != menor or meio == menor != maior or maior == menor != meio:
        print('TRIANGULO ISOSCELES')
