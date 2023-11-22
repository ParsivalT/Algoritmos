#include <stdio.h>
#include <stdbool.h>
#include "insertion_sort.h" // Inclui o arquivo de cabeçalho (header file) para a função insertion_sort

// Função que verifica se a lista está ordenada
bool verifica_lista(int lista[], int tamanho){
    for (int i=0; i < tamanho - 1; i++){
        if (lista[i] > lista[i + 1]){
            return false; // Retorna falso se encontrar elementos fora de ordem na lista
        }
    }
    return true; // Retorna verdadeiro se a lista estiver ordenada
}

int main(void){
    // Arrays de teste
    int array1[] = {9, 2, 4, 6, 5, 3, 1};
    int tamanho1 = sizeof(array1) / sizeof(array1[0]);

    int array2[] = {23, 3, 43, 2, 7, 34, 56};
    int tamanho2 = sizeof(array2) / sizeof(array2[0]);

    // Ordena os arrays usando a função insertion_sort
    insertion_sort(array1, tamanho1);
    insertion_sort(array2, tamanho2);

    // Verifica se os arrays estão ordenados e imprime os resultados
    if (verifica_lista(array1, tamanho1)){
        printf("\nTeste 1: Passou"); // Imprime se o Teste 1 passou
    } else {
        printf("\nTeste 1: Falhou"); // Imprime se o Teste 1 falhou
    }

    if (verifica_lista(array2, tamanho2)){
        printf("\nTeste 2: Passou\n"); // Imprime se o Teste 2 passou
    } else {
        printf("\nTeste 2: Falhou\n"); // Imprime se o Teste 2 falhou
    }

    return 0;
}
