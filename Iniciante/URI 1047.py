global horas, minutos


def horaIgual(Hi, Mi, Hf, Mf):
    if Hi == Hf:
        if Mi == Mf:
            horas = 24
            minutos = 0
        elif Mi > Mf:
            horas = 23
            minutos = Mf + (60 - Mi)
        else:
            horas = 0
            minutos = Mf - Mi
        valores = {'hora': horas, 'minuto': minutos}
        return valores
    else:
        return False


def horaInicialMaior(Hi, Mi, Hf, Mf):
    if Hi > Hf:
        horas = (24 - Hi) + Hf
        if Mi == Mf:
            minutos = 0
        elif Mi > Mf:
            horas = horas - 1
            minutos = (60 - Mi) + Mf
        else:
            minutos = Mf - Mi
        valores = {'hora': horas, 'minuto': minutos}
        return valores
    else:
        return False


def horaFinalMaior(Hi, Mi, Hf, Mf):
    if Hi < Hf:
        horas = Hf - Hi
        if Mi == Mf:
            minutos = 0
        elif Mi > Mf:
            horas = horas - 1
            minutos = (60 - Mi) + Mf
        else:
            minutos = Mf - Mi
        valores = {'hora': horas, 'minuto': minutos}
        return valores
    else:
        return False


horaInicio, minutoInicio, horaFinal, minutoFinal = input().split()
horaInicio = int(horaInicio)
minutoInicio = int(minutoInicio)
horaFinal = int(horaFinal)
minutoFinal = int(minutoFinal)
if horaInicio == horaFinal:
    valores = horaIgual(horaInicio, minutoInicio, horaFinal, minutoFinal)
    hora = valores['hora']
    minuto = valores['minuto']
elif horaInicio > horaFinal:
    valores = horaInicialMaior(horaInicio, minutoInicio, horaFinal, minutoFinal)
    hora = valores['hora']
    minuto = valores['minuto']
elif horaInicio < horaFinal:
    valores = horaFinalMaior(horaInicio, minutoInicio, horaFinal, minutoFinal)
    hora = valores['hora']
    minuto = valores['minuto']
print(f'O JOGO DUROU {hora} HORA(S) E {minuto} MINUTO(S)')