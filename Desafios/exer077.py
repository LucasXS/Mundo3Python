# tupla com várias palavras (não usar acentos). Dps, mostre para cada palavra quais são as suas vogais

palavras = ('maca', 'pera', 'melancia', 'banana', 'goiaba', 'acerola')
for contPalavras in palavras:
    print(f'\nNa palavra {contPalavras.upper()} temos as vogais ', end= ' ')
    for letra in contPalavras: # para cada letra na palavra P
        if letra.lower() in 'aeiou':
            print(letra, end= ' ')
