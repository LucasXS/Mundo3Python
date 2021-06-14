def metade(preco=0):
    total = preco / 2
    return total


def dobro(preco=0):
    total = preco * 2
    return total


def aumentar(preco=0, taxa=0):
    total = preco + (preco * taxa/100)
    return total


def diminuir(preco=0, taxa=0):
    total = preco - (preco * taxa / 100)
    return total


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>8.2f}'.replace('.', ',')