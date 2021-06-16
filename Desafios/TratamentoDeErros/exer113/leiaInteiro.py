"""DESAFIO 113 - Reescreva a função leiaInt() que fizemos no DESAFIO 104, incluindo agora a possibilidade da
digitação de um número de tipo inválido. Aprovete e crie também uma função leiaFloat() com a mesma funcionalidade"""


def leiaInt(mensagem):
    while True:
        try:
            num = int(input(mensagem))
        except (ValueError, TypeError):
            print('\033[1:31mERRO - DIGITE UM NÚMERO INTEIRO VÁLIDO.\033[m')
                # joga no while mais uma vez
        except KeyboardInterrupt:
            print('\n\033[1:31mEntrada de dados interrompida pelo usuário\033[m')
            return 0
        else:
            return num


def leiaFloat(mensagem):
    while True:
        try:
            num = float(input(mensagem))
        except (ValueError, TypeError):
            print('\033[1:31mERRO - DIGITE UM NÚMERO REAL VÁLIDO.\033[m')
            continue    # joga no while mais uma vez
        except KeyboardInterrupt:
            print('\n\n\033[1:31mEntrada de dados interrompida pelo usuário\033[m')
            return 0
        else:
            return num






