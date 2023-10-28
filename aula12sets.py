# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
s6 = set('Luiz')
s6 = set()  # vazio
s6 = {'Luiz', 1, 2, 3}  # com dados

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Seus valores serão sempre únicos;
# - Não aceitam valores mutáveis;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)
l1 = [1, 2, 3, 3, 3, 3, 3, 1]
s5 = set(l1)
l2 = list(s6)
s5 = {1, 2, 3}
print(3 not in s5)
for numero in s5:
    print(numero)

# Métodos úteis:
# add, update, clear, discard

s6 = set()
s6.add('Luiz')
s6.add(1)
s6.update(('Olá mundo', 1, 2, 3, 4))
# s1.clear()
s6.discard('Olá mundo')
s6.discard('Luiz')
print(s6)

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

s4 = {1, 2, 3}
s5 = {2, 3, 4}
s6 = s4 | s5
print(s6)
s6 = s4 & s5
print(s6)
s6 = s5 - s4
print(s6)
s6 = s4 ^ s5
print(s6)