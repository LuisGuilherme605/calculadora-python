"""Testes unitários das operações matemáticas da calculadora."""

import math

import pytest

from calculadora import operacoes


def test_soma():
    assert operacoes.soma(2, 3) == 5
    assert operacoes.soma(-1, 1) == 0


def test_subtracao():
    assert operacoes.subtracao(10, 4) == 6


def test_multiplicacao():
    assert operacoes.multiplicacao(3, 4) == 12


def test_divisao():
    assert operacoes.divisao(10, 2) == 5


def test_divisao_por_zero():
    with pytest.raises(ZeroDivisionError):
        operacoes.divisao(1, 0)


def test_potencia():
    assert operacoes.potencia(2, 10) == 1024


def test_raiz_quadrada():
    assert operacoes.raiz_quadrada(9) == 3


def test_raiz_quadrada_negativa():
    with pytest.raises(ValueError):
        operacoes.raiz_quadrada(-4)


def test_resto():
    assert operacoes.resto(10, 3) == 1


def test_resto_por_zero():
    with pytest.raises(ZeroDivisionError):
        operacoes.resto(1, 0)


def test_porcentagem():
    assert operacoes.porcentagem(200, 10) == 20


def test_valor_absoluto():
    assert operacoes.valor_absoluto(-7) == 7


def test_fatorial():
    assert operacoes.fatorial(5) == 120
    assert operacoes.fatorial(0) == 1


def test_fatorial_negativo():
    with pytest.raises(ValueError):
        operacoes.fatorial(-1)


def test_maior_e_menor():
    assert operacoes.maior(3, 8) == 8
    assert operacoes.menor(3, 8) == 3


def test_media():
    assert operacoes.media(4, 6) == 5


def test_dobro_triplo():
    assert operacoes.dobro(5) == 10
    assert operacoes.triplo(5) == 15


def test_quadrado_cubo():
    assert operacoes.quadrado(4) == 16
    assert operacoes.cubo(3) == 27


def test_inverso():
    assert operacoes.inverso(4) == 0.25


def test_inverso_de_zero():
    with pytest.raises(ZeroDivisionError):
        operacoes.inverso(0)


def test_eh_par():
    assert operacoes.eh_par(4) is True
    assert operacoes.eh_par(7) is False


@pytest.mark.parametrize(
    "a, b, esperado",
    [(5, 3, 1), (2, 9, -1), (4, 4, 0)],
)
def test_comparar(a, b, esperado):
    assert operacoes.comparar(a, b) == esperado


def test_raiz_quadrada_irracional():
    assert operacoes.raiz_quadrada(2) == pytest.approx(math.sqrt(2))
