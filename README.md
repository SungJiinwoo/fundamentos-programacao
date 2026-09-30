# Fundamentos de programação

Quando eu comecei, muita coisa só fez sentido porque alguém tinha deixado um
repositório ou uma explicação simples na internet. Este é o meu jeito de devolver
isso: um caderno com a base da programação, explicada do jeito que eu gostaria de
ter lido no primeiro semestre.

Cada assunto tem três partes. A anotação explica o conceito e o que costuma
confundir no começo. Os exercícios mostram o conceito em código. E os testes
conferem que o código faz o que a anotação diz.

A base é em Python, porque deixa a ideia do algoritmo mais visível. Onde o
Python esconde o que o computador está fazendo (memória, ponteiros, tamanho dos
tipos), entra C, lado a lado com a versão em Python. A parte de banco de dados
vai ser em SQL.

## Como rodar

Precisa de Python 3.12 e pytest. Para as partes em C, do gcc (no Windows, o MinGW);
sem ele, os testes de C são pulados.

```bash
pip install pytest
python -m pytest -q
```

Para ver os exercícios rodando:

```bash
python 01-logica/exercicios.py
python 02-funcoes-e-recursao/exercicios.py
```

## Trilha

| # | Assunto | Estado |
|---|---|---|
| 01 | [Lógica: variáveis, condicionais e laços](01-logica/anotacoes.md) | feito |
| 02 | [Funções e recursão](02-funcoes-e-recursao/anotacoes.md) | feito |
| 03 | [Memória: como o computador guarda os dados (em C)](03-memoria/anotacoes.md) | feito |
| 04 | Estruturas de dados: listas, pilhas, filas, dicionários e árvores (Python e C) | próximo |
| 05 | Algoritmos: busca, ordenação e complexidade | |
| 06 | Orientação a objetos | |
| 07 | Banco de dados: modelagem, SQL, índices e transações | |

HTTP, APIs, git, testes, segurança e arquitetura continuam no
[engenharia-de-software-na-pratica](https://github.com/SungJiinwoo/engenharia-de-software-na-pratica),
que é o passo seguinte depois daqui.

Se você está começando e algo aqui não ficou claro, abre uma issue. Se ficou
confuso para você, provavelmente ficou para mais gente.
