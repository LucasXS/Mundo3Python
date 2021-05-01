"""" #DESAFIO 84 - Programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) - Quantas pessoas foram cadastradas.
B) - Uma listagem com as pessoas mais pesadas.
C) - Uma listagem com as pessoas mais leves.
"""
maiorPeso = menorPeso = 0
listaDePessoas = list()
temporaria = list()

while True:
    temporaria.append(str(input('Nome: ')))
    temporaria.append(float(input('Peso: ')))
    if len(listaDePessoas) == 0:
        maiorPeso = menorPeso = temporaria[1]
    else:
        if temporaria[1] > maiorPeso:
            maiorPeso = temporaria[1]
        if temporaria[1] < menorPeso:
            menorPeso = temporaria[1]
    listaDePessoas.append(temporaria[:])
    temporaria.clear()
    continuar = input('Quer continuar? [S|N] ').upper().strip()[0]
    if continuar == 'N':
        break

print(f'Foram cadastradas {len(listaDePessoas)} pessoas')
print(f'O MAIOR peso foi de {maiorPeso}Kg. Peso de ', end='')
for posicao in listaDePessoas:
    if posicao[1] == maiorPeso:
        print(f'[{posicao[0]}]', end='')
print()

print(f'O MENOR peso foi de {menorPeso}Kg. Peso de ', end='')
for posicao in listaDePessoas:
    if posicao[1] == menorPeso:
        print(f'[{posicao[0]}]')
print()