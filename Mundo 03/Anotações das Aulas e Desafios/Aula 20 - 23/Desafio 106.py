"""
DESAFIO 106: Sistema interativo de ajuda em Python

Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra 'FIM', o programa se encerrará.
"""


def ajuda(com):
    help(com)


def titulo(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)

#programa principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PythonHELP')
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!')