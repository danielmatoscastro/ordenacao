from aleatorio import lista_aleatoria
from math import floor


def bubblesort(lista):
    for i in range(len(lista)-2, -1, -1):
        for j in range(i+1):
            if lista[j] > lista[j+1]:
                aux = lista[j+1]
                lista[j+1] = lista[j]
                lista[j] = aux


def particiona(lista, pi, pf):
    pp = pi
    i = pi + 1
    j = pf

    while j > i:
        while lista[i] <= lista[pp] and i < pf:
            i += 1
        while lista[j] > lista[pp] and j > pi:
            j -= 1
        if lista[i] > lista[j] and i < j:
            aux = lista[i]
            lista[i] = lista[j]
            lista[j] = aux

    aux = lista[j]
    lista[j] = lista[pp]
    lista[pp] = aux

    return j


def quicksort(lista, inicio, fim):
    if inicio < fim:
        pivo = particiona(lista, inicio, fim)
        quicksort(lista, inicio, pivo-1)
        quicksort(lista, pivo+1, fim)


if __name__ == '__main__':
    lista = lista_aleatoria(10)
    print(lista)
    particiona(lista, 0, len(lista)-1)
    print(lista)
