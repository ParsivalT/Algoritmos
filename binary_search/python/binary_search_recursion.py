# Função que realiza a busca binária de forma recursiva em uma lista ordenada.
def binary_search(list: list, start: int, end: int, value: int) -> int:
    # Retorna -1 caso o valor procurado não esteja presente na lista.
    if start > end:
        return -1 
    
    # Encontra o índice do meio da lista e obtém o valor correspondente.
    mid = (start + end) // 2
    current_value = list[mid]

    # Verifica se o valor procurado está no índice do meio.
    if current_value == value:
        return mid
    
    # Chama recursivamente a função com uma nova faixa à esquerda do índice do meio.
    # Isso é feito se o valor atual for maior que o valor procurado.
    if current_value > value:
        return binary_search(list=list, start=start, end=mid - 1, value=value)
    
    # Chama recursivamente a função com uma nova faixa à direita do índice do meio.
    # Isso é feito se o valor atual for menor que o valor procurado.
    if current_value < value:
        return binary_search(list=list, start=mid + 1, end=end, value=value)
    

if __name__ == "__main__":  
    data = [2, 4, 5, 6, 8, 9, 11, 15, 17]

    # Exemplo de uso da função de busca binária.
    print(binary_search(data, 0, len(data) - 1, 8))
