"""DESAFIO 086 - Crie um programa que crie uma MATRIZ de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final, mostre a MATRIZ na tela, com a formação correta."""

# cria uma Matriz vazia de 3 linhas
matriz = [[], [], []]
for i in range(0, 3):       # LINHAS
    for j in range(0, 3):   # COLUNAS
        # vai adicionados números de entrada na LINHA
        matriz[i].append(int(input(f'Digite o valor para [\033[1:34m{i}, {j}\033[m]: ')))

for i in range(0, 3):
    for j in range(0, 3):
        print(f'[\033[1:31m{matriz[i][j]:^5}\033[m]', end='')
    print()
