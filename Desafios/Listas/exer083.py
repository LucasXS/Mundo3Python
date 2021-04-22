"""EXERCICIO 083
Crie um programa onde o usuário uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se
a expressão passada está com os parênteses abertos e fechados na ordem correta.
"""
expre
ssao = str(input('Digite sua expressão: '))
pilha = []
for simbolo in expressao:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')