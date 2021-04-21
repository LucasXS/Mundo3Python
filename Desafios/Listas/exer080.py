"""
Crie um program onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posção correta
de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
"""

minhalista = []
print('=-'*25)
print('DIGITE 5 NÚMEROS SEM REPETIR NENHUM')
print('=-'*25)

for c in range(1, 6):
    num = int(input('Digte um valor: '))
    # PRIMEIRO NÚMERO - LOOP
    if c == 1:
        minhalista.append(num)
        print(f'Adicionado ao final da lista...{c}')
        valor1 = num
    else:
        # SEGUNDO NÚMERO - LOOP
        if c == 2 and num < valor1:
            minhalista.insert(0, num)
            print(f'Adicionado na posição 0 da lista...{c}')
            valor2 = num
        elif c == 2 and num > valor1:
            minhalista.append(num)
            print(f'Adicionado ao final da lista {c}')
            valor2 = num

        # TERCEIRO NÚMERO - LOOP
        if c == 3 and num < valor1 and num > valor2:
            minhalista.insert(1, num)
            print(f'Adicionado na posição 1 da lista...{c}')
            valor3 = num
        elif c == 3 and num < valor2 and num < valor1:
            minhalista.insert(0, num)
            print(f'Adicionado na posição 0 da lista...{c}')
            valor3 = num
        elif c == 3 and num > valor2 and num > valor1:
            minhalista.append(num)
            print(f'Adicionado ao final da lista...{c}')
            valor3 = num
        elif c == 3 and num < valor2 and num > valor1:
            minhalista.insert(1, num)
            print('Adicionando a posição 2 da lista...')
            valor3 = num

        # QUARTO NÚMERO - LOOP
        if c == 4 and num > valor1 and num > valor2 and num > valor3:
            minhalista.append(num)
            print(f'Adicionado ao final da lista... {c}')
            valor4 = num
        elif c == 4 and num < valor1 and num < valor2 and num < valor3:
            minhalista.insert(0, num)
            print('Adicionado a posição 0 da lista...')
            valor4 = num
        elif c == 4 and num < valor1 and num > valor2 and num > valor3:
            minhalista.insert(2, num)
            print('Adicionado a posição 2 da lista...')
            valor4 = num
        elif c == 4 and num < valor1 and num < valor2 and num > valor3:
            minhalista.insert(1, num)
            print('Adicionado a posição 1 da lista...')
            valor4 = num
        elif c == 4 and num > valor1 and num < valor2 and num > valor3:
            minhalista.insert(2, num)
            print('Adicionando a posição 2 da lista...')


      # QUINTO NÚMERO - LOOP
        """ if c == 5 and num > valor1 and num > valor2 and num > valor3 and num > valor4:
            minhalista.append(num)
            print(f'Adicionado ao final da lista... {c}')
            valor5 = num
        elif c == 5 and num < valor1 and num < valor2 and num < valor3 and num < valor4:
            minhalista.insert(0, num)
            print('Adicionado a posição 0 da lista...')
            valor5 = num
        elif c == 5 and num < valor1 and num < valor2 and num < valor3 and num > valor4:
            minhalista.insert(3, num)
            print('Adicionado a posição 3 da lista...')
            valor5 = num
        elif c == 5 and num < valor1 and num < valor2 and num > valor3 and num > valor4:
            minhalista.insert(2, num)
            print('Adicionado a posição 2 da lista...')
            valor5 = num
        elif c == 5 and num < valor1 and num > valor2 and num > valor3 and num > valor4:
            minhalista.insert(1, num)
            print('Adicionado a posição 1 da lista...')
            valor5 = num            
        elif c == 5 and num < valor1 and num > valor2 and num > valor3 and num > valor4:
            minhalista.insert(1, num)
            print('Adicionado a posição 1 da lista...')
            valor5 = num
    """

print(f'A lista {minhalista}')

