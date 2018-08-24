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
    #meio = meio if meio >= 0 else 0

    if lista[meio] == elemento or inicio >= fim:
        return meio
    elif lista[meio] < elemento:
        return busca_binaria(lista, meio+1, fim, elemento)
    else:
        return busca_binaria(lista, inicio, meio-1, elemento)


def insertionsort_busca_binaria(lista):
    for i in range(len(lista)):
        elemento = lista[i]
        j = i-1 #if i-1 >= 0 else 0

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


if __name__ == '__main__':
    lista = lista_aleatoria(10)
    print(lista)

    insertionsort_busca_binaria(lista)
    print(lista)
