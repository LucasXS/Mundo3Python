from time import sleep as sl

"""DESAFIO 099 - Faça um programa que tenha uma FUNÇÃO chamada MAIOR(), que receba vários PARÂMETROS
com valores Inteiros;
Seu programa tem que analisar todos os valores e dizer qual deles é o MAIOR"""


def maior(* valores):
    cont = maior = 0
    print()
    print('-'*30)
    print('Analisando os valores passados...')
    for valor in valores:
        print(f'{valor} ', end='', flush=True)
        sl(0.25)
        if cont == 0:
            maior = cont
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0, 1)
maior(7, 9, 10)
maior(0, 0, 0, 0)
