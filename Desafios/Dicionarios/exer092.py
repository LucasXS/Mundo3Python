"""DESAFIO 092 - Crie um programa que leia NOME, ANO DE NASCIMENTO e CARTEIRA DE TRABALHO e cadastre-os (com IDADE) em
um DICIONÁRIO se por acaso o CTPS for diferente de ZERO, o dicionário receberá também o ANO DE CONTRATAÇÃO e o SALÁRIO.
Calcule e acrescente, além da IDADE, com quantos anos a pessoa vai APOSENTAR."""

from datetime import date
anoAtual = date.today().year

ficha = {'Nome': '', 'Ano': '', 'CTPS': ''}
ficha['Nome'] = str(input('Digite seu nome: ')).upper()
ficha['Ano'] = int(input('Ano de nascimento: '))
ficha['CTPS'] = str(input('Número da carteira:'))

while ficha['CTPS'] != '0':
    ficha['AnoCont'] = int(input('Ano de contratação: '))
    ficha['Salario'] = float(input('Salario: R$'))
    ficha['Idade'] = anoAtual - ficha['Ano']
    ficha['Aposentadoria'] = (ficha['AnoCont'] + 35)
    break

for k, v in ficha.items():
    print(f'{k} tem o valor {v}')
