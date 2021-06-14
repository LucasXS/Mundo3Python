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


def resumo(preco=0, taxa_aumento=0, taxa_reducao=0):
    print('-'*30)
    print(' RESUMO DE VALOR')
    print('-'*30)

    print(f'Preço analisado: R${preco}')
    print(f'Dobro do preço:  R${dobro(preco)}')
    print(f'Metade do preço: R${metade(preco)}')
    print(f'{taxa_aumento}% de aumento: R${aumentar(preco, taxa_aumento)}')
    print(f'{taxa_reducao}% de redução: R${diminuir(preco, taxa_reducao)}')
    return preco

