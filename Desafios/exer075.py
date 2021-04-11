# ler 4 valores pelo teclado e quarde-os em uma tupla. No final, mostre:
# A-Qnt vezes apareceu o valor 9 B - Em que posição foi digitado o primeiro valor 3. C-Quais foram os números pares
cont = 0
valores = tuple(int(input('Digite valores: '))
for contador in range(1, 5))
print(f'O numero nove aparece {valores.count(9)} vez(es) na tupla')
if 3 in valores: # se 3 estiver em valores
    print(f'O três aparece primeiramente na {valores.index(3)+1}ª posição')
else:
    print('O valor três não aparece na tupla')
for n in valores:
    if n % 2 == 0:
        cont += 1
print(f'Apareceream {cont} números pares na lista')