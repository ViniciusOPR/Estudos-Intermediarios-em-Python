# Exercicios com funções

"""
Crie uma função que multiplica todos os argumentos não nomeados recebidos.
Retorne o total para uma variavel e mostre o valor da variavel

Crie uma função que fala se um número é par ou impar. Retorne se o número é par ou impar.
"""

def multiplica(*args):
    total = 1
    for numero in args:
        total *= numero
    return int(total)

multiplica_5_10 = multiplica(5, 10)
print(multiplica_5_10)

def par_impar(n):
    if n % 2 == 0 :
        return f'{n} É par'
    return f'{n} É impar'

print(par_impar(4))
print(par_impar(5))

