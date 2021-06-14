def metade(preco=0, formatado=False):
    total = preco / 2
    return total if formatado is False else moeda(total)


def dobro(preco=0, formatado=False):
    total = preco * 2
    return total if formatado is False else moeda(total)


def aumentar(preco=0, taxa=0, formatado=False):
    total = preco + (preco * taxa/100)
    return total if formatado is False else moeda(total)


def diminuir(preco=0, taxa=0, formatado=False):
    total = preco - (preco * taxa / 100)
    return total if formatado is False else moeda(total)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>2.2f}'.replace('.', ',')
