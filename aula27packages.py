from sys import path

import aula27pacotes.modulo
from aula27pacotes import modulo
from aula27pacotes.modulo import *
from aula27pacotes.modulo import soma_do_modulo, fala_oi

# from aula99_package.modulo import soma_do_modulo

# print(*path, sep='\n')

print(soma_do_modulo(1, 2))
print(aula27pacotes.modulo.soma_do_modulo(1, 2))
print(modulo.soma_do_modulo(1, 2))
print(variavel)
print(nova_variavel)

print(__name__)
fala_oi()
