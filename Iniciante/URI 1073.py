numero = int(input())
for x in range(numero + 1):
    if x % 2 == 0 and x != 0:
        print(f'{x}^2 = {pow(x,2)}')