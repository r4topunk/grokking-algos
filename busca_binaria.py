def busca_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = int((baixo + alto) / 2)
        chute = lista[meio]
        if chute == item:
            return meio
        if chute > item:
            alto = meio
        else:
            baixo = meio + 1
    return None

minha_lista = [1, 3, 7, 9]

print(busca_binaria(minha_lista, 3))
print(busca_binaria(minha_lista, 11))
