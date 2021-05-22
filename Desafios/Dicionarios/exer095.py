""" DESAFIO 095 - Aprimore o exercicios 093 para que ele funcione com vários jogadores, incluindo um sistema de
visualização de detalhes do aproveitamento de cada jogador."""

# INICIALIZAÇÕES
partidas = list()
jogador = dict()
jogadores = list()

#PROGRAMA
# LOOP DA LEITURA DOS DADOS
while True:
    # Limpando o dicionário a cada LOOP
    jogador.clear()
    jogador['nome'] = str(input('NOME DO JOGADOR: ')).upper()
    totalPartidas = int(input(f'QUANTAS PARTIDAS \033[1:33m{jogador["nome"]}\033[m DISPUTOU: '))
    # Limpando a lista a cada LOOP
    partidas.clear()
    for cont in range(0, totalPartidas):
        partidas.append(int(input(f'QUANTOS GOLS FEZ NA {cont+1}º PARTIDA: ')))
    # Guardando uma copia dos gols no dicionário JOGADOR
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    # Guardando uma copia do DICIONÁRIO na LISTA
    jogadores.append(jogador.copy())

    # LOOP DA LER MAIS DADOS
    while True:
        continuar = str(input('Deseja continuar? [S/N]')).upper()
        if continuar[0] in 'SN':
            break
        print('ERRO! Responda apenas com S ou N.')
    if continuar[0] == 'N':
        break

# RESULTADOS
print('*'*30)

# LAÇO PARA O CABEÇALHO
print(f'cod ', end='')
for indice in jogador.keys():
    print(f'{indice:<15}', end='')
print()

# LOOP PARA MOSTRAR OS DADOS
for key, valor in enumerate(jogadores):
    print(f'{key:>3}', end='')
    for dado in valor.values():
        print(f'{str(dado):<15}', end='')
    print()
print()

# LOOP PARA OS DADOS INDIVIDUAIS
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(jogadores):
        print(f'ERRO! Não existe jogador de codigo {busca}')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[busca]["nome"]}')
        for indice, g in enumerate(jogadores[busca]['gols']):
            print(f'    No jogo {indice + 1} fez {g} gols')
    print('-'*40)
print('<< VOLTE SEMPRE >>')