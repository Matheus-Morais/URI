positivo = 0
for x in range(6):
    numero = float(input())
    if numero > 0:
        positivo += 1
print(f'{positivo} valores positivos')