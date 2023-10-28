"""
Introdução às funções (def) em Python
Funções são trechos de código usados para 
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos) 
e retornar um valor específico.
Por padrão, funções Python retornam None (nada).
"""

# def Print(a, b, c):
#     print('Várias1')
#     print('Várias2')
#     print('Várias3')
#     print('Várias4')

# def imprimir(a, b, c):
#     print(a, b, c)


# imprimir(1, 2, 3)
# imprimir(4, 5, 6)

def saudacao(nome='Sem Nome'):
    print(f'Olá, {nome}')

saudacao('Luiz Otávio')
saudacao('Maria')
saudacao('Helena')
saudacao()

"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

def soma(x, y, z):
    # Definição
    print(f'{x=} y={y} {z=}', '|', 'x + y + z= ', x + y + z)

soma(1, 2, 3)
soma(1, y=2, z=5)

print(1, 2, 3, sep='-')

"""
Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem ter valores padrão.
Caso o valor não seja enviado para o parâmetro, o valor padrão será usado.
Refatorar: editar o seu código
"""

def mult(x, y, z=None):
    if z is not None:
        print(f'{x=} {y=} {z=}', x * y * z)
    else:
        print(f'{x=} {y=}', x * y)

mult(1, 2)
mult(3, 5)
mult(100, 200, 2)
