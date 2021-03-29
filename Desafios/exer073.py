# Crie uma tupla preenchida com os 20 primeiros colocados na Tabela do CBF, na ordem de colocação. Depois mostre:
# A - Apenas os 5 primeiros colocados. # B - Os últimos 4 colocados
# C - Uma lista com os times em ordem alfabética. # D - Em que posição na tabela está op time do Bahia.

times = ('SÃO PAULO', 'FLAMENGO', 'INTERNACIONAL', 'GRÊMIO',
         'PALMEIRAS', 'ATLÉTICO-MG', 'ATHLETICO', 'CRUZEIRO', 'BOTAFOGO',
         'SANTOS', 'BAHIA', 'FLUMINENSE', 'CORINTHIANS', 'CHAPECOENSE',
         'CEARÁ', 'VASCO', 'SPORT', 'AMÉRICA-MG', 'VITÓRIA', 'PARANÁ')

print('CLASSIFICAÇÃO CAMPEONATO BRASILEIRO')
print(f'Os primeiros 5 colocados: {times[:4]}')
print(f'Os últimos 4 colocados: {times[16:]}')
print(f'Ordem Alfabetica: {sorted(times)}')
print('O Bahia está na posição {}ª posição.'.format(times.index('BAHIA')+1))
