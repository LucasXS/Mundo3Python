"""brasil = []
estado1 = {'UF': 'Rio de Janeiro', 'SIGLA': 'RJ'}
estado2 = {'UF': 'Sao Paulo', 'SIGLA': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[0]['SIGLA'])
print(brasil[1]['UF'])
"""
# No dicionário não dá para fazer o fatiamento para copiar um dict
# Usamos o metodo próprio chamado .copy()

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())    # cria uma copia do dict
for e in brasil:    # FOR DA LISTA
    for k, v in e.items():      # FOR DO DICIONÁRIO
        print(f'O campo {k} tem valor {v}')