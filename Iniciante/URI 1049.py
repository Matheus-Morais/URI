osso = input()
especie = input()
alimentacao = input()
if osso == 'vertebrado':
    if especie == 'ave':
        if alimentacao == 'carnivoro':
            print('aguia')
        elif alimentacao == 'onivoro':
            print('pomba')
    elif especie == 'mamifero':
        if alimentacao == 'herbivoro':
            print('vaca')
        elif alimentacao == 'onivoro':
            print('homem')
elif osso == 'invertebrado':
    if especie == 'inseto':
        if alimentacao == 'hematofago':
            print('pulga')
        elif alimentacao == 'herbivoro':
            print('lagarta')
    elif especie == 'anelideo':
        if alimentacao == 'hematofago':
            print('sanguessuga')
        elif alimentacao == 'onivoro':
            print('minhoca')
