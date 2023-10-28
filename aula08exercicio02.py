"""
Crie funções que duplicam, triplicam e quadriplicam um número recebido como parâmetro
"""
"""
# forma simples

def duplicar(n):
    return n * 2

def triplicar(n):
    return n * 3

def quadruplicar(n):
    return n * 4

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))
"""

# Com closure

def operador(multiplicador):
    def operando(n):
        return n * multiplicador
    return operando

duplicando = operador(2)
triplicando = operador(3)
quadruplicando = operador(4)

for n in [2]:
    print(duplicando(n))
    print(triplicando(n))
    print(quadruplicando(n))
