quantidade = int(input())
contIN = 0
contOUT = 0
for x in range(quantidade):
    numero = int(input())
    if 10 <= numero <= 20:
        contIN += 1
    else:
        contOUT += 1
print(f'{contIN} in\n{contOUT} out')