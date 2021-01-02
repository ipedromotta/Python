"""
EXERCÍCIO 102: Função para Fatorial

Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular
e o outro chamado show, que será um valor lógico(opcional) indicando se será mostrado ou não na tela o processo de
cálculo do fatorial.
"""
def fatorial(n, show=False):
    """
    --> Calcula o Fatorial de um número.
    :param n: O número a ser calculado
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    fat = 1
    for c in range(n, 0, -1):
        if show:
            if c > 1:
                print(f'{c} x ', end='')
            else:
                print(c, end='')
                print(' = ', end='')
        fat *= c
    return fat


#programa principal
print(fatorial(5, True))
help(fatorial)