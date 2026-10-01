import importlib.util
import shutil
import subprocess
from pathlib import Path

import pytest

PASTA = Path(__file__).parent.parent / "04-estruturas-de-dados"
spec = importlib.util.spec_from_file_location("estruturas", PASTA / "estruturas.py")
estruturas = importlib.util.module_from_spec(spec)
spec.loader.exec_module(estruturas)
gcc = shutil.which("gcc")


def test_pilha_inverte():
    assert estruturas.inverter("pilha") == "ahlip"
    assert estruturas.inverter("") == ""


def test_parenteses():
    assert estruturas.parenteses_balanceados("(a[b]{c})")
    assert estruturas.parenteses_balanceados("")
    assert not estruturas.parenteses_balanceados("(a[b)]")
    assert not estruturas.parenteses_balanceados("((")
    assert not estruturas.parenteses_balanceados(")")


def test_fila_atende_na_ordem():
    assert estruturas.atender(["Ana", "Bruno", "Carla"]) == ["Ana", "Bruno", "Carla"]


def test_tabela_hash_com_colisao():
    tabela = estruturas.nova_tabela(4)
    for nome, nota in [("ana", 9), ("bruno", 7), ("carla", 8), ("davi", 6)]:
        estruturas.guardar(tabela, nome, nota)
    estruturas.guardar(tabela, "bruno", 10)
    assert estruturas.buscar(tabela, "carla") == 8
    assert estruturas.buscar(tabela, "bruno") == 10
    assert estruturas.buscar(tabela, "edu") is None
    assert tabela[0] == [["ana", 9], ["davi", 6]]  # a colisão da tabela das anotações


def test_hash_da_tabela_das_anotacoes():
    assert estruturas.hash_texto("ana") == 96724
    assert estruturas.hash_texto("davi") == 3076080


def test_arvore_em_ordem_e_busca():
    raiz = None
    for v in [50, 30, 70, 20, 40, 60, 80]:
        raiz = estruturas.inserir(raiz, v)
    assert estruturas.em_ordem(raiz) == [20, 30, 40, 50, 60, 70, 80]
    assert estruturas.contem(raiz, 60) == (True, 3)
    assert estruturas.contem(raiz, 65) == (False, 3)
    assert estruturas.altura(raiz) == 3


def test_ordem_de_insercao_muda_a_altura():
    torta = estruturas.arvore_em_ordem_crescente(1023)
    equilibrada = estruturas.arvore_equilibrada(1023)
    assert estruturas.altura(torta) == 1023
    assert estruturas.altura(equilibrada) == 10
    assert estruturas.contem(torta, 1023) == (True, 1023)
    assert estruturas.contem(equilibrada, 1023) == (True, 10)
    assert estruturas.em_ordem(equilibrada) == list(range(1, 1024))


def test_inserir_com_e_sem_recursao_dao_a_mesma_arvore():
    valores = [8, 3, 10, 1, 6, 14, 4, 7, 13]
    a = b = None
    for v in valores:
        a = estruturas.inserir(a, v)
        b = estruturas.inserir_laco(b, v)
    assert a == b


@pytest.fixture(scope="module")
def saida_c(tmp_path_factory):
    if not gcc:
        pytest.skip("gcc não encontrado")
    exe = tmp_path_factory.mktemp("c") / "lista_ligada"
    subprocess.run([gcc, "-Wall", "-Wextra", "-Werror", "-std=c99", "-o", str(exe), str(PASTA / "lista_ligada.c")], check=True)
    return subprocess.run([str(exe)], capture_output=True, text=True, check=True).stdout


def test_no_e_int_mais_ponteiro(saida_c):
    linha = next(l for l in saida_c.splitlines() if l.startswith("int:"))
    partes = linha.replace(":", "").split()
    assert int(partes[1]) + int(partes[4]) == int(partes[7])


def test_lista_ligada_insere_e_remove(saida_c):
    assert "10 -> 20 -> 30 -> NULL" in saida_c
    assert "remover 20: 1" in saida_c
    assert "remover 99: 0" in saida_c
    assert "10 -> 30 -> NULL" in saida_c
    assert "nos liberados: 2" in saida_c


def test_pilha_em_c(saida_c):
    assert "desempilhando: 3 2 1" in saida_c
