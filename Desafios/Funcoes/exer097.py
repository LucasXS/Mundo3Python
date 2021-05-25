"""DESAFIO 097 - Faça um programa qye tenha uma FUNÇÃO chamada ESCREVA(), que receba um texto qualquer como
PARÂMENTRO e mostre uma mensagem com tamanho adaptável."""


def escreva(txt):
    print('-' * len(txt))
    print(txt)
    print('-' * len(txt))


txt = str(input('Seu texto: '))
escreva(txt)