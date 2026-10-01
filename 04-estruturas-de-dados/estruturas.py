# Estruturas de dados em Python: pilha, fila, tabela hash e árvore binária de busca
from collections import deque


# 1. Pilha: o último que entra é o primeiro que sai.
#    A lista do Python já serve: append empilha, pop desempilha (pelo fim).
def inverter(texto):
    pilha = []
    for letra in texto:
        pilha.append(letra)
    resultado = ""
    while pilha:
        resultado += pilha.pop()
    return resultado


def parenteses_balanceados(texto):
    pares = {")": "(", "]": "[", "}": "{"}
    pilha = []
    for c in texto:
        if c in "([{":
            pilha.append(c)
        elif c in pares:
            if not pilha or pilha.pop() != pares[c]:
                return False
    return not pilha  # sobrou alguém aberto?


# 2. Fila: o primeiro que entra é o primeiro que sai.
#    deque tira do começo sem precisar empurrar o resto, ao contrário de list.pop(0).
def atender(clientes):
    fila = deque(clientes)
    ordem = []
    while fila:
        ordem.append(fila.popleft())
    return ordem


# 3. Tabela hash: é a ideia por trás do dict.
#    A chave vira um número (hash), o número vira uma posição (resto da divisão).
#    Duas chaves na mesma posição = colisão; aqui cada posição guarda uma lista de pares.
def hash_texto(chave):
    h = 0
    for letra in chave:
        h = h * 31 + ord(letra)
    return h


def nova_tabela(tamanho):
    return [[] for _ in range(tamanho)]


def guardar(tabela, chave, valor):
    posicao = hash_texto(chave) % len(tabela)
    for par in tabela[posicao]:
        if par[0] == chave:
            par[1] = valor  # chave já existe: troca o valor
            return
    tabela[posicao].append([chave, valor])


def buscar(tabela, chave):
    posicao = hash_texto(chave) % len(tabela)
    for par in tabela[posicao]:
        if par[0] == chave:
            return par[1]
    return None


# 4. Árvore binária de busca: menor vai para a esquerda, maior para a direita.
#    Cada nó é um dicionário com o valor e os dois filhos.
def inserir(raiz, valor):
    if raiz is None:
        return {"valor": valor, "esq": None, "dir": None}
    if valor < raiz["valor"]:
        raiz["esq"] = inserir(raiz["esq"], valor)
    else:
        raiz["dir"] = inserir(raiz["dir"], valor)
    return raiz


def contem(raiz, valor):
    """Devolve (achou, quantos nós foram olhados)."""
    olhados = 0
    atual = raiz
    while atual is not None:
        olhados += 1
        if valor == atual["valor"]:
            return True, olhados
        atual = atual["esq"] if valor < atual["valor"] else atual["dir"]
    return False, olhados


def em_ordem(raiz):
    if raiz is None:
        return []
    return em_ordem(raiz["esq"]) + [raiz["valor"]] + em_ordem(raiz["dir"])


def altura(raiz):
    # Feita com laço (uma fila por nível) porque, na árvore torta, a recursão
    # passaria do limite de chamadas do Python.
    if raiz is None:
        return 0
    nivel = [raiz]
    niveis = 0
    while nivel:
        niveis += 1
        nivel = [f for no in nivel for f in (no["esq"], no["dir"]) if f is not None]
    return niveis


def arvore_em_ordem_crescente(n):
    raiz = None
    for v in range(1, n + 1):
        raiz = inserir_laco(raiz, v)
    return raiz


def arvore_equilibrada(n):
    raiz = None
    for v in ordem_do_meio(1, n):
        raiz = inserir_laco(raiz, v)
    return raiz


def ordem_do_meio(ini, fim):
    # Insere primeiro o do meio, depois o meio de cada metade, e assim por diante.
    if ini > fim:
        return []
    meio = (ini + fim) // 2
    return [meio] + ordem_do_meio(ini, meio - 1) + ordem_do_meio(meio + 1, fim)


def inserir_laco(raiz, valor):
    # Mesma coisa que inserir(), sem recursão (pelo mesmo motivo da altura).
    novo = {"valor": valor, "esq": None, "dir": None}
    if raiz is None:
        return novo
    atual = raiz
    while True:
        lado = "esq" if valor < atual["valor"] else "dir"
        if atual[lado] is None:
            atual[lado] = novo
            return raiz
        atual = atual[lado]


if __name__ == "__main__":
    print("== Pilha ==")
    print("inverter('pilha') =", inverter("pilha"))
    print("'(a[b]{c})' balanceado:", parenteses_balanceados("(a[b]{c})"))
    print("'(a[b)]' balanceado:", parenteses_balanceados("(a[b)]"))

    print("\n== Fila ==")
    print("ordem de atendimento:", atender(["Ana", "Bruno", "Carla"]))

    print("\n== Tabela hash ==")
    tabela = nova_tabela(4)
    for nome, nota in [("ana", 9), ("bruno", 7), ("carla", 8), ("davi", 6)]:
        guardar(tabela, nome, nota)
    guardar(tabela, "bruno", 10)
    print("nota da carla:", buscar(tabela, "carla"))
    print("nota do bruno:", buscar(tabela, "bruno"))
    print("nota do edu:", buscar(tabela, "edu"))
    for i, posicao in enumerate(tabela):
        if posicao:
            print(f"posição {i}: {posicao}")

    print("\n== Árvore binária de busca ==")
    raiz = None
    for v in [50, 30, 70, 20, 40, 60, 80]:
        raiz = inserir(raiz, v)
    print("em ordem:", em_ordem(raiz))
    print("contém 60:", contem(raiz, 60))
    print("contém 65:", contem(raiz, 65))

    n = 1023
    torta = arvore_em_ordem_crescente(n)
    equilibrada = arvore_equilibrada(n)
    print(f"\n{n} valores inseridos em ordem crescente: altura {altura(torta)}, "
          f"buscar o {n} olha {contem(torta, n)[1]} nós")
    print(f"{n} valores inseridos a partir do meio: altura {altura(equilibrada)}, "
          f"buscar o {n} olha {contem(equilibrada, n)[1]} nós")
