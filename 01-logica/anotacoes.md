# 01. Lógica: variáveis, condicionais e laços

## O que eu preciso saber daqui

Todo programa, por maior que seja, é feito de três coisas: guardar valores
(variáveis), escolher um caminho (condicionais) e repetir (laços). Se essas três
estão firmes, o resto é combinação delas.

## Variáveis

Uma variável é um nome apontando para um valor. `total = 0` não é uma equação,
é uma ordem: "guarde 0 com o nome total". Por isso `total = total + 1` faz
sentido em programação e não faz em matemática. Lê-se da direita para a
esquerda: calcula `total + 1` e guarda de volta em `total`.

## Condicionais

`if` testa uma condição que vale `True` ou `False`. O `%` (resto da divisão) é
o melhor amigo aqui: `n % 2 == 0` quer dizer "a divisão por 2 não sobra nada",
ou seja, o número é par.

No `maior_de_tres` eu começo com `maior = a` e vou comparando um por um. É a
mesma ideia de procurar o maior valor numa lista inteira: assume o primeiro e
troca sempre que aparecer alguém maior. Comparar tudo de uma vez com `and`
funciona para três números, mas não escala.

## Laços

`for` é para quando eu sei quantas vezes vou repetir. `while` é para quando eu
repito até uma condição mudar.

Cuidado com o `range`: `range(1, 11)` vai de 1 até **10**. O último número
nunca entra. Na soma de 1 até n, por isso, o código usa `range(1, n + 1)`.

## Por que o primo testa só até a raiz

Se `n` tem um divisor maior que a raiz de `n`, ele tem obrigatoriamente um par
menor que a raiz. Exemplo com 36: 2 × 18, 3 × 12, 4 × 9, 6 × 6. Depois do 6, os
pares só se repetem invertidos. Então, se nada até a raiz divide `n`, nada
depois vai dividir. Testar `i * i <= n` é o mesmo que `i <= raiz(n)`, sem
precisar calcular raiz.

Para 1.000.003, isso é a diferença entre umas mil divisões e um milhão.

## O que costuma confundir no começo

- `=` guarda um valor, `==` compara. `if n = 0` é erro em Python.
- Laço infinito: no `while`, se nada dentro do laço muda a condição, ele nunca
  para. No `eh_primo`, é o `i += 1` que garante o fim.
- Esquecer que o 1 não é primo, e que o 2 é o único primo par. Os testes
  cobrem esses dois casos de propósito.
- `return` dentro do laço encerra a função na hora. No `eh_primo`, achar um
  divisor já responde `False`, sem terminar o laço.
