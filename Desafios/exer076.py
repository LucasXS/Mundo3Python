# tupla com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços org
# os dados em forma tabular.
print('-'*30)
print('        LISTAGEM DE PREÇOS')
print('-'*30)
listagem = (('Pão', 1), ('Leite', 2.50), ('Frango', 10.90), ('Arroz', 5.25), ('Batata', 2.50))
#  A tupla LISTAGEM é formada apenas por subtuplas de dois elementos. Assim, podemos fazer um
# laço FOR andando diretamente sobre os dois elementos de cada subtupla interna:
for x, y in listagem:
    print(f'{x:.<30} {y:.2f}')
