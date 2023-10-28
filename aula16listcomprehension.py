# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.
# print(list(range(10)))

import pprint

def p (v):
    pprint.pprint(v, sort_dicts=False, width=40)


lista = []
for numero in range(10):
    lista.append(numero)
# print(lista)

lista = [numero * 2 for numero in range(10)]
print(lista)

# Mapeamento de dados em list comprehension

produtos = [
    {'nome': 'p1', 'preco': 20,},
    {'nome': 'p2', 'preco': 10,},
    {'nome': 'p3', 'preco': 30,},
]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]

# print (novos_produtos)
print(*novos_produtos, sep='\n')

# filter em list comprehension

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if (produto['preco']) >= 20 and (produto ['preco'] * 1.05 ) > 10
]
p(novos_produtos)

#list comprehension com mais de um for

lista2 = []
for x in range(3):
    for y in range(3):
        lista2.append((x, y))

lista2 = [
    (x, y)
    for x in range(3)
    for y in range(3)
]
lista2 = [
    [(x, letra) for letra in 'luiz']
    for x in range (3)
]
print(lista2)

# mais exemplos

nomes = ['luiz', 'maria', 'helena', 'joana', 'vinicius']
novos_nomes = [f'{nome[:-1].lower()}{nome[-1].upper()}' for nome in nomes]
print(novos_nomes)

string = 'Otávio Miranda'
numero_de_letras = 2
nova_string = '.'.join([string[indice:indice + numero_de_letras] for indice in range(0, len(string), numero_de_letras)])
print(nova_string)

def div(x, y):
    return x / y

def mult(x, y):
    return x * y

ns = [1, 2, 3, 4, 5]
divisao = [div(n, 2) for n in ns]
multiplicacao = [mult(n, 2) for n in ns]

print(ns)
print(multiplicacao)
print(divisao)

algarismos = [[algarismo, algarismo ** 2] for algarismo in range(10)]
flat = [y for x in algarismos for y in x]
print(algarismos)
print(flat)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
novo_numeros = [numero for numero in numeros if numero > 5]
pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]
outro_if = [numero if numero !=6 else 600 for numero in pares]
print(numeros)
print(novo_numeros)
print(pares)
print(impares)
print(outro_if)