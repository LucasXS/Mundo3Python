# DESAFIO 88
# Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos
# serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.#

from time import sleep
from random import randint

listaJogos = []
num = 0
cont = 1
print('-'*40)
print('    JOGA NA MEGA SENA    ')
print('-'*40)
num = int(input('Quantas jogos você quer sortear? '))
for cont in range(0, num):
    for num in range(0, 6):
        listaJogos.append(randint(1, 60))
    sleep(0.5)
    print(f'Jogo {cont+1}: {sorted(listaJogos)}')
    listaJogos.clear()
sleep(0.5)
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)