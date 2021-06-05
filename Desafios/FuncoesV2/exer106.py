"""DESÁFIO 106 - Faça um mini-sistema que utilize o INTERACTIVE HELP do python. O usuário vai diigitar o COMANDO e o
MANUAL vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará.
OBS: use cores."""
from time import sleep


cores = ('\033[0;30;m',  # 0 - Sem cor
        '\033[0;30;41m', # 1 - vermelho
        '\033[0;30;42m', # 2 - verde
        '\033[0;30;43m', # 3 - amarelo
        '\033[0;30;44m', # 4 - azul
        '\033[0;30;45m', # 5 - roxo
        '\033[7;30m',   # 6 - branco
 )


def ajuda(biblioteca):
    titulo(f'Acessando o manual do comando \'{biblioteca}\'', 4)
    print(cores[6], end='')
    help(biblioteca)
    print(cores[0], end='')
    sleep(1)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(cores[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(cores[0], end='')
    sleep(1)


# programa principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca: '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 1)