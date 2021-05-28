"""DESAFIO 102 - Crie um programa que tenha uma FUNÇÃO FATORIAL() que receba dois parâmetros: o primeiro que indique
o número a calcular e o outro chamado SHOW, que será um valor LÓGICO (OPCIONAL) indicando se será mostrado ou não
na tela o processo de cáclulo do fatorial.
"""


def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número
    :param num: O número a ser calculado.
    :param show: (opcional) Mostra ou não a conta.
    :return: O valor Fatorial de um número num
    """
    f = 1
    for c in range(num, 0, -1):
        f *= c
        if show:
            print(f'{c} ', end='-> ')
    return f


print(fatorial(5, show=True))
