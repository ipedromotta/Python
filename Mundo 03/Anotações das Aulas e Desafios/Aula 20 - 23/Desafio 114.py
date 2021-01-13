"""
DESAFIO 114: Site está acessível?

Crie um código em Python que teste se o site Pudim está acessível pelo computador usado.
"""
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('Não foi possível acessar o site.')
else:
    print('Site acessado com sucesso.')
