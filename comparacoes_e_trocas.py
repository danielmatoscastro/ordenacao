from aleatorio import lista_aleatoria
from math import floor


def bubblesort(lista):
    for i in range(len(lista)-2, -1, -1):
        for j in range(i+1):
            if lista[j] > lista[j+1]:
                aux = lista[j+1]
                lista[j+1] = lista[j]
                lista[j] = aux


def combsort(lista, fator=1.3):
    gap = floor(len(lista) / fator)

    while gap >= 1:
        for k in range(0, gap):
            for i in range(k+gap, len(lista), gap):
                if lista[i] < lista[i-gap]:
                    aux = lista[i]
                    lista[i] = lista[i-gap]
                    lista[i-gap] = aux
        gap = floor(gap / fator)


if __name__ == '__main__':
    lista = lista_aleatoria(10)
    print(lista)
    combsort(lista)
    print(lista)
