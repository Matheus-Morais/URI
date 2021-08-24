def validaEntrada(A, B):
    if 1 <= A <= 1000 and 1 <= B <= 1000:
        return True
    else:
        return False


coluna = int(input())
linha = int(input())
if validaEntrada(coluna, linha):
    if coluna % 2 == 0:
        if linha % 2 == 0:
            cor = "1"
        else:
            cor = "0"
    elif coluna % 2 != 0:
        if linha % 2 != 0:
            cor = "1"
        else:
            cor = "0"
print(cor)