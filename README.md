# Fundamentos de programação

Quando eu comecei, muita coisa só fez sentido porque alguém tinha deixado um
repositório ou uma explicação simples na internet. Este é o meu jeito de devolver
isso: um caderno com a base da programação, explicada do jeito que eu gostaria de
ter lido no primeiro semestre.

Cada assunto tem três partes. A anotação explica o conceito e o que costuma
confundir no começo. Os exercícios mostram o conceito em código. E os testes
conferem que o código faz o que a anotação diz.

Os exemplos são em Python, porque deixa a lógica mais visível. A parte de banco de
dados vai ser em SQL.

## Como rodar

Precisa de Python 3.12 e pytest.

```bash
pip install pytest
python -m pytest -q
```

Para ver os exercícios rodando:

```bash
python 01-logica/exercicios.py
```

## Trilha

| # | Assunto | Estado |
|---|---|---|
| 01 | [Lógica: variáveis, condicionais e laços](01-logica/anotacoes.md) | feito |
| 02 | Funções e recursão | próximo |
| 03 | Estruturas de dados: listas, pilhas, filas, dicionários e árvores | |
| 04 | Algoritmos: busca, ordenação e complexidade | |
| 05 | Orientação a objetos | |
| 06 | Banco de dados: modelagem, SQL, índices e transações | |
| 07 | HTTP e APIs REST | |
| 08 | Git além do básico | |
| 09 | Testes automatizados | |
| 10 | Segurança básica (OWASP) | |
| 11 | Arquitetura: camadas e SOLID | |

Se você está começando e algo aqui não ficou claro, abre uma issue. Se ficou
confuso para você, provavelmente ficou para mais gente.
