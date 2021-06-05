"""DESAFIO 104 - Crie um programa que tenha a função LEIAINT(), que vai funcionar de forma semelhante a função INPUT()
do Python, só que fazendo a validação para aceitar apenas 1 valor numerico."""


def leiaInt(mensagem):
    ok = False
    valor = 0
    while True:
        num = str(input(mensagem))
        if num.isnumeric():
            valor = int(num)
            ok = True
        else:
            print('\033[1:31mERRO - DIGITE UM NÚMERO INTEIRO VÁLIDO.\033[m')
        if ok:
            break
    return valor


# programa principal
numero = leiaInt("Digite um número inteiro: ")
print(f'O número digitado foi {numero}')
