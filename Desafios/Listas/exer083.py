"""EXERCICIO 083
Crie um programa onde o usuário uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se
a expressão passada está com os parênteses abertos e fechados na ordem correta.
"""

lista = []

expressao = str(input('Digite sua expressão: '))

if expressao.count('(') == expressao.count(')'):
    lista.append(expressao)
    print('Expressão valida!')
else:
    print('Expressão invalida!')
