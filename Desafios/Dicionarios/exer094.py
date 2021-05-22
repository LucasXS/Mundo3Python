"""DESAFIO 094 - Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um
DICIONÁRIO e todos os dicionários em uma LISTA. No final mostre:
A. Quantas pessoas cadastradas
B. A média de idade.
C. Uma lista com MULHERES.
d. Uma lista com IDADE acima da MÉDIA."""

galera = list()
pessoa = dict()
continuar = ''
soma = media = 0
while continuar != 'N':
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: ')).upper()
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    pessoa['sexo'] = str(input('Sexo:[F/M] ')).upper().strip()
    while True:
        if pessoa['sexo'][0] != 'F' and pessoa['sexo'][0] != 'M':
            print('Digite o sexo corretamente sua MULA!')
            pessoa['sexo'] = str(input('Sexo:[F/M] ')).upper().strip()
        else:
            break
    galera.append(pessoa.copy())
    continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break

print(f'Ao todo temos {len(galera)} pessoas cadastradas ')
media = soma / len(galera)
print(f'A Média de idade é {media:5.2f} anos')

print('As mulheres cadastradas foram ', end=' ')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end=' ')
print()

print('PESSOAS ACIMA DA MÉDIA')
for p in galera:
    if p['idade'] > media:
        print(f'{p["nome"]} com {p["idade"]} anos')
print()