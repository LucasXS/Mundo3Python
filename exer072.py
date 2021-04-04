# Crie um programa que tenha yna TUPLA totalmente preenchida com uma contagem por extenso de ZERO até VINTE.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte',)
num = int(input('Digite um número entre 0 e 20: '))
while num != len(tupla):
    if num < 0 or num > 20:
        print('Tente novamente. Digite um número entre 0 e 20: ')
        num = int(input('Digite um número entre 0 e 20: '))
    else:
        break
print(f'Você digitou {tupla[num]}')
