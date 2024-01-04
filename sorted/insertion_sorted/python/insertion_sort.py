import random

# Função para a ordenação de uma lista com o algoritmo INSERTION SORTED
def insertion_sorted(lista):

    # Percorreno a lista apartir da segunda posição até a ultima.
    for indice in range(1, len(lista)):
        # Pegando o valor da posição atual da lista.
        valor_atual = lista[indice]

        # Definindo a posição do elemento anterior na lista.
        posicao = indice - 1

        while posicao >=0 and valor_atual < lista[posicao]:
            lista[posicao + 1] = lista[posicao]
            posicao -= 1

        lista[posicao + 1] = valor_atual


if __name__ == "__main__":
    dados = [i for i in range(1000)]
    dados = random.sample(dados, 100)

    print(dados)