/* Memória: como o computador guarda os dados.
 * Compilar e rodar:
 *   gcc -Wall -Wextra -o memoria 03-memoria/memoria.c
 *   ./memoria
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
    /* 1. Cada tipo ocupa um tamanho fixo, em bytes. O tamanho exato depende
     *    da máquina e do compilador: por isso existe o sizeof. */
    printf("== 1. Tamanho dos tipos ==\n");
    printf("char:    %zu byte\n", sizeof(char));
    printf("int:     %zu bytes\n", sizeof(int));
    printf("long:    %zu bytes\n", sizeof(long));
    printf("double:  %zu bytes\n", sizeof(double));
    printf("ponteiro: %zu bytes\n", sizeof(int *));

    /* 2. Toda variável mora num endereço. Um ponteiro guarda esse endereço. */
    printf("\n== 2. Endereço e ponteiro ==\n");
    int x = 42;
    int *p = &x;          /* & = "endereço de" */
    printf("x = %d\n", x);
    *p = 7;               /* * = "o valor que está no endereço" */
    printf("depois de *p = 7, x = %d\n", x);

    /* 3. Vetor é um bloco contínuo. v[i] é o mesmo que *(v + i). */
    printf("\n== 3. Vetor e aritmética de ponteiro ==\n");
    int v[4] = {10, 20, 30, 40};
    printf("v[2] = %d\n", v[2]);
    printf("*(v + 2) = %d\n", *(v + 2));
    printf("distancia entre v[0] e v[1]: %d bytes\n",
           (int)((char *)&v[1] - (char *)&v[0]));

    /* 4. String em C é um vetor de char terminado em '\0'. */
    printf("\n== 4. String ==\n");
    char nome[] = "oi";
    printf("strlen(\"oi\") = %zu\n", strlen(nome));
    printf("sizeof(\"oi\") = %zu\n", sizeof(nome));
    printf("ultimo byte = %d\n", nome[2]);

    /* 5. Pilha x heap. Variáveis locais ficam na pilha e somem quando a
     *    função termina. O que eu peço com malloc fica no heap até eu dar free. */
    printf("\n== 5. Heap: malloc e free ==\n");
    int n = 5;
    int *numeros = malloc(n * sizeof(int));
    if (numeros == NULL) {
        printf("sem memoria\n");
        return 1;
    }
    int soma = 0;
    for (int i = 0; i < n; i++) {
        numeros[i] = i * i;
        soma += numeros[i];
    }
    printf("soma dos quadrados de 0 a 4 = %d\n", soma);
    free(numeros);        /* esquecer isso é vazamento de memória */
    numeros = NULL;       /* evita usar o endereço depois do free */

    /* 6. Tipo com tamanho fixo tem limite. Sem sinal, passar do limite volta
     *    para zero. (Com sinal, estourar é comportamento indefinido em C.) */
    printf("\n== 6. Limite de um tipo ==\n");
    unsigned char byte = 255;
    byte = byte + 1;
    printf("unsigned char 255 + 1 = %d\n", byte);

    return 0;
}
