"""DESAFIO 103 - Faça um programa que tenha uma FUNÇÃO chamada FICHA(), que receba dois PARÂMETROS OPCIONAIS: o NOME
de um jogador e quantos GOLS ele marcou.
O Programa deverá ser capaz de mostrar a FICHA DO JOGADOR, mesmo que algum dado não tenha sido informado corretamente
"""


def fichar(nm='<desconhecido>', g=0):
    print(f'O jogador {nm} fez {g} gol(s) no campeonato')


# PROGRAMA PRINCIPAL
jogador = str(input('Nome do jogador: '))
gols = str(input('Gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if jogador.strip() == '':
    fichar(g=gols)
else:
    fichar(jogador, gols)