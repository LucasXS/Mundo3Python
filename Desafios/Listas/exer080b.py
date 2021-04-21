minhalista = []
for c in range(0, 5):
    num = int(input('Digte um valor: '))
    # se ele for o 1º OU o NUM for maior que o maior número da lista faça o append
    if c == 0 or num > minhalista[-1]:   # len(minhalista)-1
        minhalista.append(num)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(minhalista):
            if num <= minhalista[pos]:
                minhalista.insert(pos, num)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print(f'Os valores digitados em ordem foram {minhalista}')
