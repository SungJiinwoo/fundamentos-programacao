# 02. Funções e recursão

## O que eu preciso saber daqui

Função é um pedaço de código com nome, que recebe valores (parâmetros) e
devolve um resultado (`return`). Recursão é uma função que chama ela mesma
para resolver uma versão menor do mesmo problema. Toda recursão precisa de
duas partes: o **caso base**, que responde direto e faz parar, e o **caso
recursivo**, que diminui o problema.

## Funções

Três coisas que eu confundia no começo:

- **`print` não é `return`.** `print` mostra na tela. `return` devolve o valor
  para quem chamou a função poder usar. Uma função sem `return` devolve `None`.
- **Escopo.** Uma variável criada dentro da função só existe lá dentro. É por
  isso que o contador do Fibonacci precisa do `global`: ele é de fora da função.
  Na prática, evitar `global` é melhor; aqui ele está só para medir.
- **Valor padrão mutável.** `def f(memo={})` cria o dicionário uma vez só e
  reaproveita em todas as chamadas. Por isso o `fibonacci_memo` usa
  `memo=None` e cria o dicionário dentro.

## Recursão, passo a passo

O fatorial é o exemplo clássico: 5! = 5 × 4!, e 4! = 4 × 3!, até chegar em
1! = 1, que é o caso base.

```
fatorial(5)
= 5 * fatorial(4)
= 5 * 4 * fatorial(3)
= 5 * 4 * 3 * fatorial(2)
= 5 * 4 * 3 * 2 * fatorial(1)
= 5 * 4 * 3 * 2 * 1
= 120
```

Cada chamada fica esperando a de baixo responder. O computador guarda essas
chamadas pendentes numa pilha (a *pilha de chamadas*). Se a recursão não para,
a pilha estoura. No Python o limite padrão é de mais ou menos 1000 chamadas,
e o erro é `RecursionError`.

## Por que o Fibonacci ingênuo é tão lento

`fibonacci(n)` chama `fibonacci(n-1)` e `fibonacci(n-2)`, e cada uma delas
chama mais duas. O mesmo valor é recalculado muitas vezes. Contei as chamadas
rodando o código:

| n | resultado | chamadas |
|---|---|---|
| 10 | 55 | 177 |
| 20 | 6.765 | 21.891 |
| 25 | 75.025 | 242.785 |

O número de chamadas é sempre 2 × F(n+1) − 1. Para n = 10: 2 × 89 − 1 = 177.
Ele cresce junto com o próprio Fibonacci, ou seja, exponencialmente.

A correção é guardar o que já foi calculado (memoização). Com o dicionário
`memo`, cada valor é calculado uma vez só, e `fibonacci_memo(90)` responde na
hora, enquanto a versão ingênua levaria anos.

## Recursão ou laço?

Todo problema recursivo pode ser escrito com laço, e o contrário também. O
fatorial com laço é até melhor em Python, porque não gasta pilha. A recursão
brilha quando o problema já é recursivo por natureza: árvores, pastas dentro
de pastas, dividir e conquistar (o merge sort, por exemplo).

## O que costuma confundir no começo

- Esquecer o caso base, ou escrever um caso base que nunca é alcançado.
- Não diminuir o problema: `fatorial(n)` chamando `fatorial(n)` de novo.
- Achar que recursão é sempre mais elegante. Às vezes é só mais lenta.
