"""DESAFIO 114 -
Crie um código em Python que teste se o site PUDIM está acessível pelo computador usado"""

import urllib
import urllib.request

try:
    url = urllib.request.urlopen('http://www.pudim.com.br')

except urllib.error.URLError:
    print('O site pudim não está acessivel no momento')
else:
    print('Consegue acessar o site com sucesso')
    print(url.read(), end='')