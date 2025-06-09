
def buscaMenorIndice(arr):
    print()
    print("Buscando menor em:", arr)
    menor = arr[0]
    menor_indice = 0
    for i in range(1, len(arr)):
        print(f"Testando {arr[i]}")
        if arr[i] < menor:
            print(f"{arr[i]} é menor que {menor}")
            menor = arr[i]
            menor_indice = i
    print(f"O menor valor é {menor}")
    return menor_indice

def ordenacaoPorSelecao(arr):
    novoArr = []
    for i in range(len(arr)):
        menorIndice = buscaMenorIndice(arr)
        novoArr.append(arr.pop(menorIndice))
    return novoArr

ordenacao = ordenacaoPorSelecao([5, 3, 6, 2, 10])
print(ordenacao)
