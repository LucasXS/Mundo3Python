"""DESAFIO 087 - Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores PARES digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha"""

somaPares = somaColunas = maiorValor = 0
# cria uma Matriz vazia de 3 linhas
matriz = [[], [], []]
for linha in range(0, 3):       # LINHAS
    for coluna in range(0, 3):   # COLUNAS
        # vai adicionados números de entrada na LINHA
        matriz[linha].append(int(input(f'Digite o valor para [\033[1:34m{linha}, {coluna}\033[m]: ')))
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[\033[1:31m{matriz[linha][coluna]:^5}\033[m]', end='')
        if matriz[linha][coluna] % 2 == 0:
            somaPares += matriz[linha][coluna]
    print()
for linha in range(0, 3):
    somaColunas += matriz[linha][2]

for coluna in range(0, 3):
    if coluna == 0:
        maiorValor = matriz[1][coluna]
    elif matriz[1][coluna] > maiorValor:
        maiorValor = matriz[1][c]

print('-='*30)
print(f'A soma dos valore paras é {somaPares}')
print(f'A soma dos valors da terceira coluna é {somaColunas}')
print(f'O Maior valor da segunda linha é {maiorValor}')
