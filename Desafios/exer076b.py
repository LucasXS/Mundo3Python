listagem = ('Pão', 1, 'Leite', 2.50, 'Frango', 10.90, 'Arroz', 5.25, 'Batata', 2.50)
print('-'*38)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*38)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'{listagem[pos]:.>7.2f}')
