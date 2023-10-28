try:
    a = 18
    b = 0
    # print(b[0])
    # print('Linha 1'[1000])
    c = a / b
    print('Linha 2')
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
except NameError:
    print('Nome b não está definido')
except (TypeError, IndexError) as error:
    print('TypeError + IndexError')
    print('MSG:', error)
    print('Nome:', error.__class__.__name__)
except Exception:
    print('Erro Desconhecido')

print('Continuar')

# Try_Except com Else e Finally

# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

try:
    print('Abrir Arquivo')
    8 / 0
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
    print('Dividiu Zero')
except NameError as error:
    print('NameError')
except (IndexError, ImportError):
    print('IndexError + ImportError')
else:
    print('Não deu erro')
finally:
    print('Fechar Arquivo, sempre sou executado no código')