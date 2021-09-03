numero = int(input())
cont = 1
while cont <= 6:
    if numero % 2 != 0:
        print(numero)
        numero += 1
        cont += 1
    else:
        numero += 1