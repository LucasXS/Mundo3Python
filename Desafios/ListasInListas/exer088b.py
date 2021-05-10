from time import sleep
from random import randint

lista = list()
jogos = list()
print('-'*30)
print('    JOGA NA MEA SENA    ')
print('-'*30)
quantidade = int(input('Quantos joos você quer que eu sorteie? '))
total = 1
while total <= quantidade:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print('-=' * 3, f' SORTEANDO {quantidade} JOGOS ', '-' * 3)
for i, l in enumerate(jogos):
    print(f'JOGO {i+1}: {l}')
    sleep(0.5)
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)
