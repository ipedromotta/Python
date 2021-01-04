"""
DESAFIO 104: Validando entrada de dados em Python.

Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante a função input() do Python, só que
fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt('Digite um n')
"""
def leiaInt(num):
    while True:
        valor = str(input((num)))
        if valor.isnumeric():
            return valor
        else:
            print('\033[31mERRO! Digite um número inteiro válido\033[m')
        if valor.isnumeric():
            break


#programa principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
