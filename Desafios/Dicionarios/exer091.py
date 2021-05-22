""" DESAFIO 091 - Crie um programa onde 4 JOGADORES joguem um dado e tenham resultados ALEATÓRIOS. Guarde esses
resultados em um dicionário. No final, coloque esse dicionário em ORDEM, sabendo que o vencedor tirou o MAIOR NÚMERO
no dado"""

from random import randint
from operator import itemgetter
from time import sleep

# Randomizando 4 jogadores
# Jogador = KEY | randint = VALUE | 'Jogador1': randint(1, 7) = ITEM 1
resultado = {'Jogador1': randint(1, 6), 'Jogador2': randint(1, 6),
             'Jogador3': randint(1, 6), 'Jogador4': randint(1, 6)}
ranking = list()

# Logica
print('-='*30)
print('Valores Sorteados:')
for k, v in resultado.items():
    print(f'O {k} tirou {v}')
    sleep(1)

# Colocando os resultado em ordem
print('-='*30)
print('Ranking dos Jogadores:')
ranking = sorted(resultado.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):     # enumerate pq é lista
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)
