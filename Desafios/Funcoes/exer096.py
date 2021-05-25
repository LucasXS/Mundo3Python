"""DESAFIO 096 - Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
 (largura e comprimento) e mostre a área do terreo"""


def area(larg, comprim):
    areaTotal = larg * comprim
    print(f'A área de um terreo é {larg}x{comprim} é de {areaTotal}m²')


print('  Controle de Terrero')
print('-'*20)
larg = float(input('LARGURA (M): '))
comprim = float(input('COMPRIMENTO (M): '))
area(larg, comprim)
