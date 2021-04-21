"""EXERCICIO 81 -
Cire um programa que lerá vários números e irá colocar em uma lista, depois disso, mostre:
A) Quantos número foram digitados
B) A lista de valores ordenada de forma decrescente
C) Se o valor 5 foi digitado e está ou não na lista.
"""
lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if continuar in 'Nn':
        break
print('-='*30)
print(f'Você digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem DESCRESCENTE: {lista}')
if 5 in lista:
    print('O valor 5 está na lista')
else:
    'O valor 5 não está na lista!'