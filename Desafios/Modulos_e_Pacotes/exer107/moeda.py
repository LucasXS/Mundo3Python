def metade(preco):
    total = preco / 2
    return total


def dobro(preco):
    total = preco * 2
    return total


def aumentar(preco, taxa):
    total = preco + (preco * taxa/100)
    return total


def diminuir(preco, taxa):
    total = preco - (preco * taxa / 100)
    return total