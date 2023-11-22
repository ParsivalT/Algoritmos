

def insertion_sort(lista):
    # Percorre a lista a partir do segundo elemento até o final
    for elemento in range(1, len(lista)):
        # Armazena o valor do elemento atual da lista
        valorAtual = lista[elemento] 
        
        # Define a posição do elemento anterior na lista
        posicao = elemento - 1
        
        # Enquanto a posição for válida e o elemento na posição for maior que o valor atual
        while posicao >= 0 and lista[posicao] > valorAtual:
            # Move o elemento na posição para a direita na lista para abrir espaço para o valor atual
            lista[posicao + 1] = lista[posicao]
            
            # Decrementa a posição para verificar o próximo elemento à esquerda
            posicao -= 1

        # Insere o valor atual na posição correta na lista ordenada
        lista[posicao + 1] = valorAtual
