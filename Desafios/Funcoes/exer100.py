"""DESAFIO 100 - Faça um programa que tenha uma lista chamada NÚMEROS[] e DUAS FUNÇÕES chamadas SORTEIA() e SOMAPAR().
A primeira função vai sortear 5 NÚMEROS e vai colocálos dentro da lista e a segunda função vai mostrar a SOMA entre
todos os valores PARES sorteados pela função anterior."""
from random import randint as rd
from time import sleep as sl
numeros = list()


def sorteia():
    print('SORTEANDO 5 VALORES DA LISTA')
    for i in range(0, 5):
        num = rd(1, 10)
        numeros.append(num)
        print(f'{num} ', end='')
        sl(0.3)
    print('PRONTO')


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')


sorteia()
somaPar(lista=numeros)
