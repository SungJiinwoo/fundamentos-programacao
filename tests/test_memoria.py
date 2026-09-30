import os
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

PASTA = Path(__file__).parent.parent / "03-memoria"
gcc = shutil.which("gcc")


@pytest.fixture(scope="module")
def saida_c(tmp_path_factory):
    if not gcc:
        pytest.skip("gcc não encontrado")
    exe = tmp_path_factory.mktemp("c") / "memoria"
    subprocess.run([gcc, "-Wall", "-Wextra", "-Werror", "-std=c99", "-o", str(exe), str(PASTA / "memoria.c")], check=True)
    return subprocess.run([str(exe)], capture_output=True, text=True, check=True).stdout


def test_ponteiro_muda_a_variavel(saida_c):
    assert "depois de *p = 7, x = 7" in saida_c


def test_vetor_e_aritmetica_de_ponteiro(saida_c):
    assert "v[2] = 30" in saida_c
    assert "*(v + 2) = 30" in saida_c


def test_distancia_entre_elementos_e_o_tamanho_do_int(saida_c):
    tamanho_int = next(l for l in saida_c.splitlines() if l.startswith("int:")).split()[1]
    assert f"distancia entre v[0] e v[1]: {tamanho_int} bytes" in saida_c


def test_string_tem_o_byte_zero_no_fim(saida_c):
    assert 'strlen("oi") = 2' in saida_c
    assert 'sizeof("oi") = 3' in saida_c
    assert "ultimo byte = 0" in saida_c


def test_heap(saida_c):
    assert "soma dos quadrados de 0 a 4 = 30" in saida_c  # 0 + 1 + 4 + 9 + 16


def test_unsigned_volta_para_zero(saida_c):
    assert "unsigned char 255 + 1 = 0" in saida_c


def test_python_mesmo_objeto():
    env = {**os.environ, "PYTHONIOENCODING": "utf-8"}
    saida = subprocess.run([sys.executable, str(PASTA / "memoria.py")], capture_output=True, encoding="utf-8", env=env, check=True).stdout
    assert "a = [1, 2, 3, 4]" in saida
    assert "a is b: True" in saida
    assert "255 + 1 = 256" in saida
