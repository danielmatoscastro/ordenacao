from aleatorio import lista_aleatoria
from math import floor


def bubblesort(lista):
    for i in range(len(lista)-2, -1, -1):
        for j in range(i+1):
            if lista[j] > lista[j+1]:
                aux = lista[j+1]
                lista[j+1] = lista[j]
                lista[j] = aux


# Cortesia da wikipedia :)
def combsort(lista, fator=1.3):
    gap = floor(len(lista) / fator)

    i = 0
    while gap > 0 and i < len(lista)-1:
        i = 0
        while i + gap < len(lista):
            if lista[i] < lista[i+gap]:
                aux = lista[i]
                lista[i] = lista[i+gap]
                lista[i+gap] = aux
            i = i + 1

        gap = floor(gap / fator)


def particiona(lista, pi, pf)?
    pp = pi
    i = pi + 1
    j = pf

    while j > i:
        while c[i] < c[pp] and i < pf:
            i += 1
        while c[j] > c[pp] and j > pi:
            i -= 1
        if c[i] < c[j]:
            aux = c[i]
            c[i] = c[j]
            c[j] = aux
    aux = c[j]
    c[j] = c[pp]
    c[pp] = aux

    return j


def quicksort(lista, inicio, fim):
    if fim > inicio:
        pivo = particiona(lista, inicio, fim)
        quicksort(lista, inicio, pivo-1)
        quicksort(lista, pivo+1, fim)


if __name__ == '__main__':
    lista = lista_aleatoria(10)
    print(lista)
    quicksort
    print(lista)
