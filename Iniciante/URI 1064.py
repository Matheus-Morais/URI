positivo = 0
divisor = 0
soma = 0
for x in range(6):
    numero = float(input())
    if numero > 0:
        positivo += 1
        divisor += 1
        soma += numero
print(f'{positivo} valores positivos\n{soma/divisor:.1f}')