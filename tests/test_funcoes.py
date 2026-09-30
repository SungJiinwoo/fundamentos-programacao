import importlib.util
from pathlib import Path

caminho = Path(__file__).parent.parent / "02-funcoes-e-recursao" / "exercicios.py"
spec = importlib.util.spec_from_file_location("funcoes", caminho)
funcoes = importlib.util.module_from_spec(spec)
spec.loader.exec_module(funcoes)


def test_fatorial_recursivo_e_com_laco_concordam():
    for n in range(0, 20):
        assert funcoes.fatorial(n) == funcoes.fatorial_laco(n)
    assert funcoes.fatorial(5) == 120
    assert funcoes.fatorial(0) == 1


def test_soma_digitos():
    assert funcoes.soma_digitos(1234) == 10
    assert funcoes.soma_digitos(7) == 7
    assert funcoes.soma_digitos(0) == 0


def test_palindromo():
    assert funcoes.eh_palindromo("arara")
    assert funcoes.eh_palindromo("")
    assert funcoes.eh_palindromo("a")
    assert not funcoes.eh_palindromo("python")


def fib_ingenuo_com_contagem(n):
    funcoes.chamadas = 0
    valor = funcoes.fibonacci(n)
    return valor, funcoes.chamadas


def test_numero_de_chamadas_da_tabela_das_anotacoes():
    assert fib_ingenuo_com_contagem(10) == (55, 177)
    assert fib_ingenuo_com_contagem(20) == (6765, 21891)
    assert fib_ingenuo_com_contagem(25) == (75025, 242785)


def test_chamadas_seguem_a_formula():
    # chamadas(n) = 2 * F(n+1) - 1
    for n in range(0, 20):
        _, chamadas = fib_ingenuo_com_contagem(n)
        assert chamadas == 2 * funcoes.fibonacci_memo(n + 1) - 1


def test_memoizacao_da_o_mesmo_resultado():
    for n in range(0, 25):
        assert funcoes.fibonacci_memo(n) == fib_ingenuo_com_contagem(n)[0]
    assert funcoes.fibonacci_memo(90) == 2880067194370816120
