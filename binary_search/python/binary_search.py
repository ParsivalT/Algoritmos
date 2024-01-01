def binary_search(lista:list, valor) -> int:
    inicio = 0
    fim = len(lista) - 1  # Pegando o indice da ultima posição da lista.
    
    # Enquanto o incio for menor que o final da lista segue a interação.
    while inicio <= fim:
        meio = (inicio + fim) // 2 # Pegando o indice do meio da lista.
        palpite = lista[meio] # Pegando o valor do indice no meio da lista.

        # Compara se o valor pego é igual ao procurado, caso verdadeiro retorna o indice 
        if palpite == valor:
            return meio
        
        # Verifica se o valor é maior que o procurado, caso verdadeiro o final da lista é reduzido.
        if palpite > valor:
            fim = meio - 1

        # Verifica se o valor é menor que o procurado, caso verdadeiro o inicio da lista é aumentado.
        if palpite < valor:
            inicio = meio + 1

    return - 1

