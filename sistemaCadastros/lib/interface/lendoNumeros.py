def leiaInt(mensagem):
    while True:
        try:
            num = int(input(mensagem))
        except (ValueError, TypeError):
            print('\033[1:31mERRO - DIGITE UM NÚMERO INTEIRO VÁLIDO.\033[m')
        except KeyboardInterrupt:
            print('\n\033[1:31mEntrada de dados interrompida pelo usuário\033[m')
            return 0
        else:
            return num
