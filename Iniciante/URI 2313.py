def validaTrinagulo(lado1, lado2, lado3):
    if ((abs(lado2 - lado3)) < lado1 < (lado2 + lado3)) and ((abs(lado1 - lado3)) < lado2 < (lado1 + lado3)) and (
            (abs(lado1 - lado2)) < lado3 < (lado1 + lado2)):
        return True
    else:
        return False


def trianguloEquilatero(lado1, lado2, lado3):
    if lado1 == lado2 == lado3:
        return True
    else:
        return False


def trianguloEscaleno(lado1, lado2, lado3):
    if lado1 != lado2 != lado3:
        return True
    else:
        return False


def trianguloIsoceles(lado1, lado2, lado3):
    if ((lado1 == lado2) and lado1 != lado3) or ((lado1 == lado3) and lado1 != lado2) or (
            (lado2 == lado3) and lado2 != lado1):
        return True
    else:
        return False


def trianguloRetangulo(lado1, lado2, lado3):
    maior = max(lado1, lado2, lado3)
    menor = min(lado1, lado2, lado3)
    meio = ((lado1 + lado2 + lado3) - (maior + menor))
    if (maior ** 2) == (menor ** 2) + (meio ** 2):
        return True
    else:
        return False


A, B, C = input().split()
A = int(A)
B = int(B)
C = int(C)
if validaTrinagulo(A, B, C):
    if trianguloIsoceles(A, B, C):
        if trianguloRetangulo(A, B, C):
            mensagem = 'Valido-Isoceles\nRetangulo: S'
        else:
            mensagem = 'Valido-Isoceles\nRetangulo: N'
    elif trianguloEscaleno(A, B, C):
        if trianguloRetangulo(A, B, C):
            mensagem = 'Valido-Escaleno\nRetangulo: S'
        else:
            mensagem = 'Valido-Escaleno\nRetangulo: N'
    elif trianguloEquilatero(A, B, C):
        if trianguloRetangulo(A, B, C):
            mensagem = 'Valido-Equilatero\nRetangulo: S'
        else:
            mensagem = 'Valido-Equilatero\nRetangulo: N'
else:
    mensagem = 'Invalido'
print(mensagem)
