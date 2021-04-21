# D
lista1 = []
lista2 = []
lista3 = []
while True:
    lista1.append(int(input('Digite um número: ')))
    continuar = str(input('Quer continuar? [S/N] '))
    if continuar in 'Nn':
        break
for indice, valor in enumerate(lista1):
    # números PARES
    if valor % 2 == 0:
        lista2.append(valor)
    # números IMPARES
    elif valor % 2 == 1:
        lista3.append(valor)
print('-='*30)
print(f'Lista COMPLETA: {lista1}')
print(f'Lista de PARES: {lista2}')
print(f'Lista de IMPARES:  {lista3}')