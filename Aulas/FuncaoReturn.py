"""
FUNÇÕES QUE RETORNAM RESULTADO SÃO MUITO ÚTEIS QUANDO QUEREMOS USAR O RESULTADO DE FORMA PERSONALIZADA
"""


def soma(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = soma(3, 2, 5)
r2 = soma(2, 2)
r3 = soma(6)

print(f'Os resultados foram {r1}, {r2} e {r3}')