# 04. Estruturas de dados: listas, pilhas, filas, dicionários e árvores

## O que eu preciso saber daqui

Estrutura de dados é o jeito de organizar os dados na memória para que a
operação que eu mais faço seja barata. Não existe a melhor estrutura: existe a
melhor para aquele uso. Pilha é boa para "desfazer o último", fila para
"atender na ordem", dicionário para "achar pela chave", árvore para "achar e
manter em ordem".

No Python quase tudo já vem pronto (`list`, `deque`, `dict`). Em C eu monto na
mão com `struct`, ponteiros e `malloc`, e é aí que dá para ver o que o Python
está fazendo por baixo.

Os exemplos estão em [`estruturas.py`](estruturas.py) e
[`lista_ligada.c`](lista_ligada.c).

```bash
python 04-estruturas-de-dados/estruturas.py
gcc -Wall -Wextra -o lista_ligada 04-estruturas-de-dados/lista_ligada.c
./lista_ligada
```

## Resumo

| Estrutura | Regra | No Python | Operação barata |
|---|---|---|---|
| Lista ligada | cada nó aponta para o próximo | (não precisa) | inserir no começo |
| Pilha | último a entrar, primeiro a sair | `list` com `append` e `pop()` | mexer no topo |
| Fila | primeiro a entrar, primeiro a sair | `collections.deque` | tirar do começo, pôr no fim |
| Tabela hash | a chave vira uma posição | `dict` | achar pela chave |
| Árvore binária de busca | menor à esquerda, maior à direita | (não tem pronta) | achar e manter em ordem |

## Lista ligada (em C)

No módulo de memória o vetor era um bloco contínuo. A lista ligada é o
contrário: cada elemento (nó) fica num lugar qualquer do heap e guarda o
endereço do próximo. O último aponta para `NULL`.

```c
typedef struct No {
    int valor;
    struct No *proximo;
} No;
```

No meu computador (MinGW 32 bits) um nó ocupa **8 bytes**: 4 do `int` e 4 do
ponteiro. Cada elemento paga o preço de um ponteiro a mais.

- **Inserir no começo** é barato: o nó novo aponta para o antigo primeiro e
  pronto.
- **Inserir no fim** obriga a andar a lista inteira até o último.
- **Remover** é fazer o nó anterior "pular" o removido e dar `free` nele.
- **Acessar o 500º** também obriga a andar 500 nós. No vetor é uma conta só.

Para liberar a lista inteira, eu guardo o `proximo` **antes** do `free`.
Depois do `free` o nó não é mais meu, e ler `atual->proximo` dali é usar
memória já devolvida.

As funções recebem `No **inicio` (ponteiro para ponteiro) porque às vezes
precisam mudar quem é o primeiro nó. Com `No *inicio` só, elas mudariam uma
cópia.

## Pilha

Último a entrar, primeiro a sair, como uma pilha de pratos. É a mesma ideia da
pilha de chamadas do módulo de recursão.

Em C, a pilha é a lista ligada mexendo só no começo: empilhar é inserir no
início, desempilhar é tirar o primeiro. Empilhando 1, 2 e 3, sai **3 2 1**.

No Python, a própria `list` serve, com `append` e `pop()` pelo fim. A
documentação mostra isso em
[Using Lists as Stacks](https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-stacks).

Um uso clássico é conferir parênteses: cada `(`, `[` ou `{` entra na pilha, e
cada fechamento tem que bater com o que está no topo. `(a[b]{c})` passa,
`(a[b)]` não.

## Fila

Primeiro a entrar, primeiro a sair, como fila de banco.

Daria para usar `list` com `pop(0)`, mas a documentação diz que é lento: tirar
do começo obriga todos os outros elementos a andarem uma posição
([Using Lists as Queues](https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-queues)).
O certo é [`collections.deque`](https://docs.python.org/3/library/collections.html#collections.deque),
que tira e coloca nas duas pontas com custo O(1), enquanto `list.pop(0)` custa
O(n).

## Tabela hash (o que o `dict` é por dentro)

A ideia: transformar a chave num número (o *hash*) e usar o resto da divisão
pelo tamanho da tabela como posição. Assim eu vou direto na posição certa, sem
procurar a tabela toda.

No exemplo eu fiz uma função de hash simples (`h = h * 31 + letra`) e uma
tabela de 4 posições:

| Chave | Hash | Posição (hash % 4) |
|---|---|---|
| ana | 96724 | 0 |
| bruno | 94017190 | 2 |
| carla | 94431305 | 1 |
| davi | 3076080 | 0 |

`ana` e `davi` caíram na mesma posição. Isso é uma **colisão**, e é normal.
Por isso cada posição guarda uma listinha de pares, e na busca eu ainda comparo
a chave dentro dela. Com poucas colisões, achar a chave continua rápido.

O `dict` do Python trabalha com essa ideia, e por isso a chave precisa ser
*hashable*: a documentação diz que um mapeamento associa valores hashable a
objetos quaisquer
([Mapping Types — dict](https://docs.python.org/3/builtins/stdtypes.html#mapping-types-dict)).
Uma lista não pode ser chave porque pode mudar, e o hash dela mudaria junto.

Detalhe: o `hash()` de uma string no Python muda de uma execução para outra,
porque leva um valor aleatório
([documentação do `__hash__`](https://docs.python.org/3/reference/datamodel.html#object.__hash__)).
Por isso eu fiz a minha própria função: para os números da tabela acima serem
sempre os mesmos.

## Árvore binária de busca

Cada nó tem até dois filhos. Regra: o que é menor vai para a esquerda, o que é
maior ou igual vai para a direita. Para buscar, eu comparo com o nó e desço só
para um lado, descartando o outro.

Inserindo 50, 30, 70, 20, 40, 60, 80, a árvore fica com 3 níveis. Buscar o 60
olha **3** nós. Percorrer "esquerda, nó, direita" devolve tudo em ordem:
`[20, 30, 40, 50, 60, 70, 80]`.

O problema é a ordem de inserção. Rodando com 1023 valores:

| Como inseri | Altura | Nós olhados para achar o 1023 |
|---|---|---|
| em ordem crescente (1, 2, 3, ...) | 1023 | 1023 |
| começando pelo meio de cada metade | 10 | 10 |

Inserindo em ordem crescente, todo valor vai para a direita e a árvore vira uma
lista ligada torta. Equilibrada, cada comparação corta o que sobra pela metade.
Existem árvores que se reequilibram sozinhas (AVL, rubro-negra), mas isso fica
para depois.

Na árvore torta eu tive que trocar a recursão por laço: com 1023 níveis, a
versão recursiva passaria do limite de chamadas do Python (o mesmo
`RecursionError` do módulo 02).

## O que costuma confundir no começo

- Achar que lista ligada é sempre melhor que vetor. Ela ganha para inserir no
  começo e perde para acessar por posição.
- Usar `list.pop(0)` como fila. Funciona, mas fica lento com muitos elementos.
- Confundir a pilha (estrutura de dados) com a pilha da memória do módulo 03.
  A ideia é a mesma, último a entrar, primeiro a sair, mas são coisas
  diferentes.
- Achar que colisão na tabela hash é erro. É esperado; o que importa é tratar.
- Achar que árvore binária de busca é sempre rápida. Depende da ordem em que os
  valores entraram.
- Esquecer de guardar o `proximo` antes do `free` ao liberar a lista em C.
