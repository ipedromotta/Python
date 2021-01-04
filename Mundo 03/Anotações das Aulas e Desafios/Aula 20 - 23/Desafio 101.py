"""
DESAFIO 101: Funções para votação

Faça um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
"""
def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if 18 <= idade < 65:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO')
    elif idade >= 65:
        print(f'Com {idade} anos: VOTO OPCIONAL')
    elif idade >= 16:
        print(f'Com {idade} anos: VOTO OPCIONAL')
    elif idade < 16:
        print(f'Com {idade} anos: NÃO VOTA')


#programa principal
print('-' * 20)
voto(int(input('Em que ano você nasceu? ')))