"""DESAFIO 101 - Crie um programa que tenha uma FUNÇÃO chamada VOTO() que vai receber como PARÂMETRO
o ANO DE NASCIMENTO de uma pessoa, RETORNANDO um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou
OBRIGATORIO nas eleições."""


def voto(ano_nascimento=1900):
    from datetime import date
    atual = date.today().year
    idade = atual - ano_nascimento
    if idade < 16:
        return f'Com {idade} anos: VOTO NEGADO'
    elif 16 <= idade < 18 or idade >= 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATORIO'


num = int(input('Em que ano você nasceu? '))
print(voto(num))
