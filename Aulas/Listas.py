
lanche = ['pizza', 'Hamburguer','Maça','Pera','Sorvete',]
lanche.append('Picole') #adiciona ao fim da lista
lanche.insert(0,'Hot-dog') #adiciona ao inicio da lista
del lanche[3] #apaga um item da lista (indece)
lanche.pop() #apaga um item da lista, por padrão ele apaga o último (indece)
lanche.remove('Sorvete') #apaga um item da lista (valor)
if 'pizza' in lanche:
    lanche.remove('pizza')
valores = list(range(4, 11))
valores2 = [8,2,5,7,12,10,0]
valores2.sort() #organiza os valores
valores2.sort(reverse=True) #organiza os valores de forma inversa

valores3 = []
valores3.append(9)
valores3.append(5)
valores3.append(4)

'''valores4 = list()
for cont in range(0,5):
    valores4.append(int(input('Digite um valor: ')))

for posicao, valor in enumerate(valores4): #enumerate pega as cheves e o valor
    print(f'Na posição {posicao} encontrei o valor {valor}')
print('Cheguei ao final da lista')'''

a = [2, 3, 4, 7]
#b = a #Cria uma LIGAÇÃO entre as lista, se alterar 1 vai alterar a outra
b = a[:] #Cria uma COPIA - [:] - em todas as posições
b[2] = 15
print(f'Lista A: {a}')
print(f'Lista B: {b}')

