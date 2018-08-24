from random import randint
from aleatorio import lista_aleatoria


def insertionsort(lista):
    for i in range(1, len(lista)):
        elemento = lista[i]
        j = i-1

        while j >= 0 and lista[j] > elemento:
            lista[j+1] = lista[j]
            j = j - 1

        lista[j+1] = elemento


if __name__ == '__main__':
    lista = lista_aleatoria(10)
    print(lista)
    insertionsort(lista)
    print(lista)
