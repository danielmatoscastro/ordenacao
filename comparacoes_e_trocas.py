from aleatorio import lista_aleatoria


def bubblesort(lista):
    for i in range(len(lista)-2, -1, -1):
        for j in range(i+1):
            if lista[j] > lista[j+1]:
                aux = lista[j+1]
                lista[j+1] = lista[j]
                lista[j] = aux


if __name__ == '__main__':
    lista = lista_aleatoria(10)
    print(lista)
    bubblesort(lista)
    print(lista)
