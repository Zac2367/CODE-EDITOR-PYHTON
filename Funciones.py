x = int(input("DAME UN NUMERO: "))
y = int(input("DAME OTRO NUMERO: "))
z = int(input("DAME OTRO NUMERO: "))

print("El numero mayor es:", max(max(x, y), z))


def max(x, y):
    """ESTA FUNCION CALCULA EL MAXIMO ENTRE DOS NUMEROS"""
    if x > y:
        maximo = x
    else:
        maximo = y
    return maximo
