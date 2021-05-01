""" DESAFIO 85 - Crie um programa onde o usuário possa digitar SETE valores numéricos e cadastre-os
em uma lista única que mantenha separadaos os valore PARES e IMPARES. No final, mostre os valores pares e
impares em ORDEM CRESCENTE."""

lista = [[], []]
for c in range(0, 7):
    num = int(input(f'Digite o {c+1}º valor: '))
    if num % 2 == 0:
        lista[0].append(num)
    elif num % 2 == 1:
        lista[1].append(num)
print(f'PARES {sorted(lista[0])} ', end=' ')
print(f'IMPARES {sorted(lista[1])}', end='')
