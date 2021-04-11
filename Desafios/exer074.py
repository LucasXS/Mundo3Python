# crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# mostre a listagem de números geradsos e também indique o menor e o maior valor que estão na tupla.

from random import randint
tupla = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print(tupla)
print(f'O Maior número foi {max(tupla)}')
print(f'O Menor número   foi o {min(tupla)}')

