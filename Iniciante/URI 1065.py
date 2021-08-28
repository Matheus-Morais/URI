pares = 0
for x in range(5):
    numero = float(input())
    if numero % 2 == 0:
        pares += 1
print(f'{pares} valores pares')