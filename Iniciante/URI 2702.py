def validaEntrada(A, B, C):
    if 0 <= A <= 100 and 0 <= B <= 100 and 0 <= C <= 100:
        return True
    else:
        return False


F1, B1, M1 = input().split()
F2, B2, M2 = input().split()
F1 = int(F1)
B1 = int(B1)
M1 = int(M1)
F2 = int(F2)
B2 = int(B2)
M2 = int(M2)
if validaEntrada(F1, B1, M1) and validaEntrada(F2, B2, M2):
    frango = 0
    bife = 0
    massa = 0
    if F1 < F2:
        frango = F2 - F1
    if B1 < B2:
        bife = B2 - B1
    if M1 < M2:
        massa = M2 - M1
    print(frango+massa+bife)


