# tuplas são IMUTAVEIS
# Eu posso ter dados de tipos diferentes dentro da Tuplica pessoa = ('lUCAS', '25', '99.15')
# del(tupla) vai apagar toda a typla
'''
a = (5, 1, 4)
b = (4, 5, 8, 2)
c = a + b
print(c)
print(f'A Tupla {c} em ordem fica: {sorted(c)}')
print(f'Quantas vezes aparece o 5 na Tupla? {c.count(5)}')
print(c)
print(f'Em que posição o 8 está? {c.index(8)}')
print(f'Depos    da posição 1, o número 5 aparece em qual posição? {c.index(5, 1)}')   # Deslocamento
'''

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')   # os parenteses não são obrigatorios

#for comida in lanche:
 #   print(f'Eu vou comer {comida}')

for cont in range(0, len(lanche)):
    print(lanche[cont])     # mostre o lanche na posição do contador

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

#print('Comi pra caramba!')
#print(sorted(lanche)) # colaca em ordem


'''print(lanche)
print(lanche[-2])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])    # 0 e 1
print(lanche[-2:])   # começa na pizza e vai até o final'''

