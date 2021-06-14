"""DESAFIO 112 - Dentro do pacote utilidadesCeV que criamos no DESAFIO 111, temos um módulo chamado DADO. Crie uma
função chamada leiaDinheiro() que seja capaz de funcionar como a função INPUT(), mas com uma VALIDAÇÃO DE DADOS
para aceitar apenas valores que sejam MONETÁRIOS"""


def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg))
        if entrada.isalpha():
            print(f'ERRO: \"{entrada}\" é um preço inválido!')
        else:
            valido = True
            return float(entrada)
