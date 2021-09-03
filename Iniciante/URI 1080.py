numero = int(input())
comparador = 0
maior = 0
posicao = 0
for i in range(99):
    numeroNovo = int(input())
    if numeroNovo > comparador:
        maior = numeroNovo
        posicao = i + 1
        comparador = numeroNovo
print(maior)
print(posicao)