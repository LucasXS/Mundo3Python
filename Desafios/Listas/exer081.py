"""EXERCICIO 81 -
Cire um programa que lerá vários números e irá colocar em uma lista, depois disso, mostre:
A) Quantos número foram digitados
B) A lista de valores ordenada de forma decrescente
C) Se o valor 5 foi digitado e está ou não na lista.
"""

lista = []
cont = 0

while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    cont += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break

print(f'Foram digitidaos {cont} números')
lista.sort(reverse=True)
print(lista)
if lista.count(5) == True:
    print('O valor 5 está na lista')
else:
    'O valor 5 não está na lista!'