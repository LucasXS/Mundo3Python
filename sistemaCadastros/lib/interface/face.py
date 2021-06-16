from sistemaCadastros.lib.interface.lendoNumeros import *


def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[1;33m{c} - {item}\033[m')
        c += 1
    print(linha())
    opcao = leiaInt('Sua Opção: ')
    return opcao
