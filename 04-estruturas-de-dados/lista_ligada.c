/* Lista ligada em C: cada nó é pedido com malloc e aponta para o próximo.
 * Compilar e rodar:
 *   gcc -Wall -Wextra -o lista_ligada 04-estruturas-de-dados/lista_ligada.c
 *   ./lista_ligada
 */
#include <stdio.h>
#include <stdlib.h>

typedef struct No {
    int valor;
    struct No *proximo;   /* endereço do próximo nó, ou NULL no último */
} No;

/* Cria um nó no heap. Quem chama fica responsável pelo free. */
No *novo_no(int valor) {
    No *no = malloc(sizeof(No));
    if (no == NULL) {
        printf("sem memoria\n");
        exit(1);
    }
    no->valor = valor;
    no->proximo = NULL;
    return no;
}

/* Coloca no começo: não precisa andar pela lista. */
void inserir_no_inicio(No **inicio, int valor) {
    No *no = novo_no(valor);
    no->proximo = *inicio;
    *inicio = no;
}

/* Coloca no fim: precisa andar até o último nó. */
void inserir_no_fim(No **inicio, int valor) {
    No *no = novo_no(valor);
    if (*inicio == NULL) {
        *inicio = no;
        return;
    }
    No *atual = *inicio;
    while (atual->proximo != NULL) {
        atual = atual->proximo;
    }
    atual->proximo = no;
}

/* Tira o primeiro nó com esse valor. Devolve 1 se achou, 0 se não. */
int remover(No **inicio, int valor) {
    No *anterior = NULL;
    No *atual = *inicio;
    while (atual != NULL && atual->valor != valor) {
        anterior = atual;
        atual = atual->proximo;
    }
    if (atual == NULL) {
        return 0;
    }
    if (anterior == NULL) {
        *inicio = atual->proximo;      /* era o primeiro */
    } else {
        anterior->proximo = atual->proximo;  /* "pula" o nó removido */
    }
    free(atual);
    return 1;
}

void imprimir(No *inicio) {
    for (No *atual = inicio; atual != NULL; atual = atual->proximo) {
        printf("%d -> ", atual->valor);
    }
    printf("NULL\n");
}

/* Libera todos os nós. Guarda o próximo ANTES do free. */
int liberar(No **inicio) {
    int liberados = 0;
    No *atual = *inicio;
    while (atual != NULL) {
        No *proximo = atual->proximo;
        free(atual);
        atual = proximo;
        liberados++;
    }
    *inicio = NULL;
    return liberados;
}

/* Pilha em cima da lista: empilhar e desempilhar mexem só no começo. */
int desempilhar(No **topo) {
    No *velho = *topo;
    int valor = velho->valor;
    *topo = velho->proximo;
    free(velho);
    return valor;
}

int main(void) {
    printf("== 1. Tamanho de um no ==\n");
    printf("int: %zu + ponteiro: %zu = no: %zu bytes\n",
           sizeof(int), sizeof(No *), sizeof(No));

    printf("\n== 2. Lista ligada ==\n");
    No *lista = NULL;
    inserir_no_fim(&lista, 20);
    inserir_no_fim(&lista, 30);
    inserir_no_inicio(&lista, 10);
    imprimir(lista);
    printf("remover 20: %d\n", remover(&lista, 20));
    printf("remover 99: %d\n", remover(&lista, 99));
    imprimir(lista);
    printf("nos liberados: %d\n", liberar(&lista));

    printf("\n== 3. Pilha (ultimo a entrar, primeiro a sair) ==\n");
    No *pilha = NULL;
    for (int i = 1; i <= 3; i++) {
        inserir_no_inicio(&pilha, i);
    }
    printf("desempilhando:");
    while (pilha != NULL) {
        printf(" %d", desempilhar(&pilha));
    }
    printf("\n");

    return 0;
}
