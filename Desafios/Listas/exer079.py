""" EXERCICIO 79
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos
digitados, em ordem crescente.
"""

minhalista = []

while True:
    continuar = ' '
    while continuar not in 'SN':
        numero = int(input('Digite um valor: '))
        if numero not in minhalista:
            minhalista.append(numero)
        else:
            print('Número duplicado')
        continuar = str(input('Quer continuar? ')).upper().strip()[0]
    if continuar == 'N':
         break
print(f'O número digitados em ordem foram {sorted(minhalista)}')


