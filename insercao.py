from math import log, floor
from aleatorio import lista_aleatoria


def insertionsort(lista):
    for i in range(1, len(lista)):
        elemento = lista[i]
        j = i-1

        while j >= 0 and lista[j] > elemento:
            lista[j+1] = lista[j]
            j = j - 1

        lista[j+1] = elemento


def busca_binaria(lista, inicio, fim, elemento):
    meio = ((fim - inicio) // 2) + inicio

    if lista[meio] == elemento or inicio >= fim:
        return meio
    elif lista[meio] < elemento:
        return busca_binaria(lista, meio+1, fim, elemento)
    else:
        return busca_binaria(lista, inicio, meio-1, elemento)


def insertionsort_busca_binaria(lista):
    for i in range(len(lista)):
        elemento = lista[i]
        j = i-1

        posicao = busca_binaria(lista, 0, j, elemento)

        if posicao != i:
            while j >= posicao:
                lista[j+1] = lista[j]
                j = j-1

        if lista[posicao] <= elemento:
            lista[posicao+1] = elemento
        else:
            lista[posicao+1] = lista[posicao]
            lista[posicao] = elemento


def insertionsort_shell(lista, h):
    for k in range(0, h):
        for i in range(k+h, len(lista), h):

            elemento = lista[i]
            j = i - h

            while j >= 0 and lista[j] > elemento:
                lista[j+h] = lista[j]
                j = j - h

            lista[j+h] = elemento


def shell_sort(lista):
    h = 2**floor(log(len(lista), 2))

    while h >= 1:
        insertionsort_shell(lista, h)
        h = h // 2


if __name__ == '__main__':
    lista = lista_aleatoria(8)
    print(lista)

    shell_sort(lista)
    print(lista)
