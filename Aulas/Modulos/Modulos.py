"""import uteisDois

num = int(input('Digite um valor: '))
fat = uteisDois.fatorial(num)
print(f'O Fatorial de {num} é {fat}')
print(f'O dobro de {num} é {uteisDois.dobro(num)} e o triplo é {uteisDois.triplo(num)}')"""


from uteisDois import numeros


num = int(input('Digite um valor: '))
fat = numeros.fatorial(num)
print(f'O Fatorial de {num} é {fat}')
print(f'O dobro de {num} é {numeros.dobro(num)} e o triplo é {numeros.triplo(num)}')