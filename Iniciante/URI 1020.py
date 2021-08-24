idadeDias = int(input())
anos = idadeDias // 365
meses = (idadeDias - anos*365) // 30
dias = (idadeDias - anos*365 - meses*30)
print(f'{anos} ano(s)')
print(f'{meses} mes(es)')
print(f'{dias} dia(s)')
