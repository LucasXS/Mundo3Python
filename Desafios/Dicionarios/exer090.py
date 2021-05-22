""" DESAFIO 090 - Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No
final, mostre o conteúdo da estrutura na tela."""

aluno = dict()      # dicionário
conteudo = list()   # lista

# Laço p/ a leitura
for cont in range(1):
    aluno['Nome'] = str(input('Nome do aluno: ')).upper()
    aluno['Media'] = float(input(f'Média de \033[1;35m{aluno["Nome"]}\033[m: '))
    if aluno["Media"] >= 7:
        aluno["Situação"] = 'Aprovado'
    else:
        aluno["Situação"] = 'Reprovado'
    conteudo.append(aluno.copy())

# Laço p/ a impressão formatada
print('-='*25)
for elemento in conteudo:
    for key, value in elemento.items():
        print(f'\033[1;31m{key}\033[m é igual a \033[1;33m{value}\033[m')
