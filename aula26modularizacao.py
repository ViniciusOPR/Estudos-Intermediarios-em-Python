# Modularização - Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por padrão
# O python conhece todos os módulos e pacotes presentes nos caminhos de sys.path

import aula26_m
from aula26_m import soma, variavel_modulo

print('Esse módulo se chama:', __name__)
print(aula26_m.variavel_modulo)
print(variavel_modulo)
print(soma(4, 3))
print(aula26_m.soma(4, 3))

print('-' * 20)

# Recarregando módulos - Importlib

import importlib

for i in range(10):
    importlib.reload(aula26_m)
    print(i)

print('FIM')