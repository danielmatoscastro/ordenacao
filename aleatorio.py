from random import randint


def lista_aleatoria(n):
    lista = []
    for i in range(n):
        lista.append(randint(0,n))
    return lista
