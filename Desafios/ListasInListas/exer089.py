# DESAFIO 89 - Crie um prorama que leia o NOME e DUAS NOTAS de vários alunos e guarde tudo em uma LISTA COMPOSTA.
# No final mostre um BOLETIM contendo a MÉDIA de cada um e permita que o usuário possa mostrar as NOTAS de cada
# aluno individualmente

lista = list()
while True:
    nome = str(input('Nome: ')).upper()
    nota1 = float(input('Nota 1:'))
    nota2 = float(input('Nota 2:'))
    media = (nota1 + nota2) /2
    lista.append([nome, [nota1, nota2], media])

    continuar = input('Quer continuar? [S|N] ').upper().strip()[0]
    if continuar != 'N':
        continue
    break

print('-=' * 15)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-=' * 15)

for i, a in enumerate(lista):   # i=Indice | a=aluno
    print(f'{i:<4}{a[0]:<8}{a[2]:>8.1f}')

while True:
    opcao = int(input('Mostra notas de qual aluno? (999 interrompe) '))
    if opcao == 999:
        print('FINALIZANDO...')
        break
    if opcao <= len(lista) - 1:
        print(f'NOTAS DE {lista[opcao][0]} SÃO {lista[opcao][1]}')
    else:
        print('Digite um valor valido!')

    print('<<< VOLTE SEMPRE >>>')