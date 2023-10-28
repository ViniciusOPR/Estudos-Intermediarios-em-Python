# raise - lançando exceções (erros)

def nao_aceito_zero(d):
    if d == 0:
        raise ZeroDivisionError('Você está tentando dividir por zero')
    return True

def deve_ser_int_ou_float(n, d):
    tipo_n = type(n)
    tipo_d = type(d)
    if not isinstance(n, (float, int)):
        raise TypeError(
            f'"{n}" deve ser int ou float.'
            f'"{tipo_n.__name__}" enviado'
        )
    if not isinstance(d, (float, int)):
        raise TypeError(
            f'"{d}" deve ser int ou float.'
            f'"{tipo_d.__name__}" enviado'
        )
    return True

def divide (n, d):
    deve_ser_int_ou_float(n, d)
    nao_aceito_zero(d)
    return n / d

print(divide(2, 1))
