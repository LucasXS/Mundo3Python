"""DESAFIO 109 - Modifique as funções que foram criadas no DESAFIO 107 oara que elas aceitem UM PARÂMETRO a mais, infor
mando se o valor retornado por elas vai ser oo não formatado pela função MOEDA(), desenvolvida no DESAFIO 108.
"""

import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10, True)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13, True)}')
