from time import sleep
"""DESAFIO 098 - Faça um programa que tenha uma função chamada CONTADOR(), que receba três parâmetros:
INICIO - FIM e PASSO e realize a contagem. Seu programa tem que realizar TRÊS CONTAGENS através da função criada.
A. De 1 até 10, de 1 em 1 | B. De 10 até 1, de 2 em 2 | C. Uma contagem personalizada"""


def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print('-='*20)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo} ')
    sleep(0.50)

    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.35)
            cont += passo
        print('FIM')
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont}', end=' ')
            sleep(0.35)
            cont -= passo
        print('FIM')


contador(1, 10, 1)
contador(10, 0, 2)
print('AGORA É SUA VEZ DE PERSONALIZAR!')
inicioL = int(input('Inicio: '))
fimL = int(input('Fim:       '))
passoL = int(input('Passo:   '))
contador(inicioL, fimL, passoL)
