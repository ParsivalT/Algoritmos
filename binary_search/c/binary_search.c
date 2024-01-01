#include <stdio.h>

int binary_search(int list[], int size, int value){
    int inicio, fim, meio, chute;

    inicio = 0;
    fim = size - 1;

    while (inicio <= fim) {
        meio = (inicio + fim);
        chute = list[meio];

        if (chute == value) {
            return meio;
        }

        if (chute > value) {
            fim = meio -1;
        }

        if (chute < value) {
            inicio = meio +1;
        }
    }   
    return -1;
}

/* Função para printar o Array */
void print_array(int list[], int size){
    for (int i=0; i<size; i++){
        printf("%d ", list[i]);
    }
    printf("\n");
}


int main(void){

    int date[] = {2, 3, 4, 5, 8, 9, 11, 13, 15, 16, 17, 19, 20, 24, 24};
    int size =  sizeof(date) / sizeof(date[0]);

    print_array(date, size);

    int index = binary_search(date, size, 5);

    printf("\nO indice do valor é %d\n", index);

    return 0;
}

