"""Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre
qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""

listNum = []
maior = 0
menor = 0
for cont in range(0, 5):
    listNum.append(int(input(f'Digite um valor na posição {cont}: ')))
    if cont == 0:
        maior = menor = listNum[cont]
    else:
        if listNum[cont] > maior:
            maior = listNum[cont]
        if listNum[cont] < menor:
            menor = listNum[cont]

for indice, valor in enumerate(listNum):
    if valor == maior:
        print(f'O Maior valor foi {valor} na {indice+1}º posição')
for indice, valor in enumerate(listNum):
    if valor == menor:
        print(f'O menor valor foi {valor} na {indice+1}º posição')

"""
for num in listNum:
    if num > maior:
        maior = num

for num in listNum:
    if num == 1:
        menor = num
    elif num < menor:
        menor = num"""



