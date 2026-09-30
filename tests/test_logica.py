import importlib.util
from pathlib import Path

caminho = Path(__file__).parent.parent / "01-logica" / "exercicios.py"
spec = importlib.util.spec_from_file_location("logica", caminho)
logica = importlib.util.module_from_spec(spec)
spec.loader.exec_module(logica)


def test_par_ou_impar():
    assert logica.par_ou_impar(0) == "par"
    assert logica.par_ou_impar(7) == "ímpar"
    assert logica.par_ou_impar(-4) == "par"


def test_maior_de_tres_em_qualquer_posicao():
    assert logica.maior_de_tres(9, 4, 2) == 9
    assert logica.maior_de_tres(4, 9, 2) == 9
    assert logica.maior_de_tres(4, 2, 9) == 9
    assert logica.maior_de_tres(5, 5, 5) == 5


def test_soma_ate_bate_com_a_formula():
    # 1 + 2 + ... + n = n(n+1)/2
    for n in range(0, 50):
        assert logica.soma_ate(n) == n * (n + 1) // 2


def test_primos_ate_30():
    primos = [n for n in range(31) if logica.eh_primo(n)]
    assert primos == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


def test_primo_casos_que_confundem():
    assert not logica.eh_primo(1)
    assert logica.eh_primo(2)
    assert not logica.eh_primo(36)  # 6 x 6: o divisor é exatamente a raiz
    assert logica.eh_primo(1_000_003)


def test_tabuada(capsys):
    logica.tabuada(3)
    linhas = capsys.readouterr().out.strip().splitlines()
    assert len(linhas) == 10
    assert linhas[0] == "3 x 1 = 3"
    assert linhas[-1] == "3 x 10 = 30"
