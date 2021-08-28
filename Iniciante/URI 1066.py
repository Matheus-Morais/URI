pares = 0
impares = 0
positivos = 0
negativos = 0
for x in range(5):
    numero = float(input())
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    if numero > 0:
        positivos += 1
    if numero < 0:
        negativos += 1
print(f'{pares} valor(es) par(es)\n{impares} valor(es) impar(es)\n{positivos} valor(es) positivo(s)\n{negativos} valor(es) negativos')
