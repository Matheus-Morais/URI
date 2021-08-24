def validaEntrada(A):
    if 0 <= A <= 2000:
        return True
    else:
        return False


D = int(input())
if validaEntrada(D):
    if D <= 800:
        ponto = 1
    elif 800 < D <= 1400:
        ponto = 2
    else:
        ponto = 3
print(ponto)