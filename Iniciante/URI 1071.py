numero1 = int(input())
numero2 = int(input())
maior = max(numero1, numero2)
menor = min(numero1, numero2) + 1
resultado = 0
while menor < maior:
    if menor % 2 != 0:
        resultado = resultado + menor
    menor += 1
print(resultado)