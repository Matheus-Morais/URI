def validaEntrada(func1, func2, func3):
    if 0 <= func1 <= 1000 and 0 <= func2 <= 1000 and 0 <= func3 <= 1000:
        return True
    else:
        return False


def primeiroAndar(func1, func2, func3):
    totalMinutos1 = (func2 * 2) + (func3 * 4) + (func1*0)
    return totalMinutos1


def segundoAndar(func1, func2, func3):
    totalMinutos2 = (func1 * 2) + (func3 * 2) + (func2*0)
    return totalMinutos2


def terceiroAndar(func1, func2, func3):
    totalMinutos3 = (func1 * 4) + (func2 * 2) + (func3*0)
    return totalMinutos3


A = int(input())
B = int(input())
C = int(input())
if validaEntrada(A, B, C):
    menor = min(primeiroAndar(A, B, C), segundoAndar(A, B, C), terceiroAndar(A, B, C))
    print(menor)