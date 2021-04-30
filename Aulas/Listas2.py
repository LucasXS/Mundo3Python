"""teste = list()
teste.append('Lucas')
teste.append(25)
galera = list()
galera.append(teste[:])     # [:] cria uma copia / SEM o [:] ele cria uma ligação entre as duas estruturas
teste[0] = 'Maria'
teste[1] = 33
galera.append(teste[:])
print(galera)"""

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
"""print(galera[0][0])
print(galera[-2][-1])
print(galera[2][1])"""

"""for p in galera:
    print(p)"""
"""for p in galera:
    print(p[1])"""
"""for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade!')"""

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
galera = list()
dado = list()
totalMaiores = totalMenores = 0

# ESTRUTURA AUXILIAR
" FUNÇÃO: Ler e jogar os dados dentrO da variavel composta GALERA, apagando os dados a cada laço"

for c in range(0,5):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

print(galera)

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de Idade!')
        totalMaiores += 1
    else:
        totalMenores +=1
        print(f'{p[0]} é menor de Idade!')

print(f'Temos {totalMaiores} maiores e {totalMenores} menores de idade!')