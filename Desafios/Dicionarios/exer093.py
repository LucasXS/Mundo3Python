""" DESAFIO 093 - Crie um programa que gerencie o aproveitamento de um JOGAR DE FUTEBOL. O programa vai ler o NOME DO JOGADOR e
QUANTAS PARTIDAS ele jogou. Depois vai ler a QUANTIDADE DE GOLS feitos em CADA PARTIDA. No final tudo isso será
guardado em um DICIONÁRIO, incluindo o TOTAL DE GOLS feitos durante o campeonato."""

# JOGADOR (Nome e Aproveitamento (lista))
partidas = list()
jogador = dict()
jogador['nome'] = str(input('Nome do Jogador: ')).upper()
total = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for cont in range(0, total):
    partidas.append(int(input(f'Quantos gols fez na {cont+1}º partida? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)

print('-='*30)
print(f'O jogador {jogador["nome"]} fez {len(jogador["gols"])} partidas')
for i, v in enumerate(jogador['gols']):
    print(f'           => Na partida {i+1}, fez {v} gols')
print(f'Foi um total de {jogador["total"]} gols')


"""print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)"""
