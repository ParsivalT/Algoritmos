#include <stdio.h>
#include "insertion_sort.h"


// Função de ordenação Insertion Sort
void insertion_sort(int lista[], int tamanho){ 
    int elemento, valorAtual, posicao;

    for (elemento = 1; elemento < tamanho; elemento++){
        valorAtual = lista[elemento];
        posicao = elemento - 1;

        // Move os elementos maiores para a direita para inserir o valorAtual na posição correta
        while (posicao >= 0 && lista[posicao] > valorAtual){
            lista[posicao + 1] = lista[posicao];
            posicao--;
        }

        lista[posicao + 1] = valorAtual; // Insere o valorAtual na posição correta
    }
}

// Função para imprimir um array
void print_array(int lista[], int tamanho){
    for (int i=0; i<tamanho; i++){
        printf("%d ", lista[i]); // Imprime cada elemento do array
    }
    printf("\n"); // Pula para uma nova linha após imprimir o array
}


