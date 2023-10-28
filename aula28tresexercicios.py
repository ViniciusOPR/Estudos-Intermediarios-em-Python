# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

import copy
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

for p in produtos:
    print(p)

print('-' * 30)


produtos_aumentados = [
    {**produto, 'preco': round(produto['preco'] * 1.10, 2)}
    for produto in produtos
]

novos_produtos = copy.deepcopy(produtos_aumentados)
for p in novos_produtos:
    print(p)

print('-' * 30)

produtos_ordenados_por_nome = copy.deepcopy(sorted(produtos, key=lambda item: item['nome'], reverse=True))
for p in produtos_ordenados_por_nome:
    print(p)

print('-' * 30)

produtos_ordenados_por_preco = copy.deepcopy(sorted(produtos, key=lambda item: item['preco']))
for p in produtos_ordenados_por_preco:
    print(p)
