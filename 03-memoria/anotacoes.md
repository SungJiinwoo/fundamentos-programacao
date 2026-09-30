# 03. Memória: como o computador guarda os dados

## O que eu preciso saber daqui

A memória é uma fila enorme de bytes, e cada byte tem um endereço. Toda
variável ocupa alguns desses bytes. Em C eu vejo e mexo nisso direto: tamanho
dos tipos, endereços, ponteiros, `malloc` e `free`. Em Python tudo isso
acontece escondido. Entender o C é entender o que o Python está fazendo por
mim.

Os exemplos estão em [`memoria.c`](memoria.c) e [`memoria.py`](memoria.py).

```bash
gcc -Wall -Wextra -o memoria 03-memoria/memoria.c
./memoria
python 03-memoria/memoria.py
```

## Tamanho dos tipos

Rodando no meu computador (Windows, compilador MinGW de 32 bits):

| Tipo | Bytes |
|---|---|
| `char` | 1 |
| `int` | 4 |
| `long` | 4 |
| `double` | 8 |
| ponteiro | 4 |

Num Linux de 64 bits, `long` e ponteiro dão **8**. O C não fixa esses
tamanhos, só garante mínimos. Por isso o certo é usar `sizeof` e nunca
escrever o número na mão.

No Python, o número `0` sozinho ocupa **28 bytes**, porque é um objeto
completo (tipo, contador de referências e o valor). Em C, um `int` são 4.
É um dos motivos de C ser tão mais rápido e econômico.

## Endereço e ponteiro

```c
int x = 42;
int *p = &x;   // p guarda o endereço de x
*p = 7;        // muda o valor que está nesse endereço: agora x vale 7
```

- `&x` é "o endereço de x".
- `*p` é "o valor que está no endereço guardado em p".

Foi o que mais me confundiu: o `*` na declaração (`int *p`) quer dizer "p é um
ponteiro", e o `*` no uso (`*p = 7`) quer dizer "vai até o endereço".

## Vetor é um bloco contínuo

`int v[4]` são 4 inteiros encostados na memória. `v[2]` e `*(v + 2)` são a
mesma coisa: o compilador anda 2 posições de `int` a partir do começo. A
distância entre `v[0]` e `v[1]` deu exatamente `sizeof(int)`, 4 bytes.

E é por isso que o C não avisa quando eu acesso `v[10]` num vetor de 4: ele só
calcula o endereço e lê o que estiver lá. É a origem do *buffer overflow*, uma
das falhas de segurança mais antigas que existem.

## String em C

String é um vetor de `char` que termina com um byte `0` (o `'\0'`). `"oi"`
ocupa **3** bytes: `o`, `i` e o `0`. Por isso `strlen("oi")` dá 2, mas
`sizeof` dá 3. Esquecer o espaço do `'\0'` é um erro clássico.

## Pilha e heap

- **Pilha:** variáveis locais. Nascem quando a função começa e somem quando ela
  termina, sozinhas. É a mesma pilha de chamadas do módulo de recursão.
- **Heap:** o que eu peço com `malloc`. Fica até eu devolver com `free`.

Três erros com o heap:

1. **Esquecer o `free`:** vazamento de memória. O programa vai ocupando cada
   vez mais.
2. **Usar depois do `free`:** o endereço pode já ser de outra coisa. Por isso
   eu zero o ponteiro (`numeros = NULL`) logo depois.
3. **Não conferir o `malloc`:** se faltar memória, ele devolve `NULL`.

No Python não existe `free`: um coletor de lixo libera o objeto quando ninguém
mais aponta para ele.

## Limite de um tipo

Um `unsigned char` vai de 0 a 255. `255 + 1` dá **0**: volta para o começo,
como um odômetro. Com tipo **com sinal** (`int`), estourar o limite é
*comportamento indefinido* em C: pode dar qualquer coisa.

No Python o `int` cresce o quanto precisar: `255 + 1` é 256, e `2 ** 100`
funciona normalmente.

## Variável no Python é uma etiqueta

```python
a = [1, 2, 3]
b = a
b.append(4)   # a também passa a ter o 4
```

`b = a` não copia a lista. As duas variáveis apontam para o **mesmo** objeto,
parecido com dois ponteiros para o mesmo endereço em C. Para copiar de verdade:
`b = a.copy()`.

## O que costuma confundir no começo

- O `*` com dois sentidos (declarar ponteiro e acessar o valor).
- Achar que `sizeof` de uma string dá o número de letras.
- No Python, achar que `b = a` fez uma cópia.
- Achar que o tamanho do `int` e do ponteiro é igual em todo computador.
