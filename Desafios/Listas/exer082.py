"""EXERCICIO 082
Crie um programa que lerá vários números e irá colocar em uma lista
Depois, crie duas listas extras que vão contar apenas os valores pares e os impares digitados, respectivamente.
Ao final, mostre o resultado das três listas geradas.

"""
lista1 = []
lista2 = []
lista3 = []
while True:
    num = int(input('Digite um número: '))
    lista1.append(num)

    # números PARES
    if num % 2 == 0:
        lista2.append(num)
    # números IMPARES
    else:
        lista3.append(num)

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break

print(f'Lista COMPLETA: {lista1}')
print(f'Lista de PARES: {lista2}')
print(f'Lista de IMPARES:  {lista3}')