"""Operações matemáticas puras da calculadora.

Cada função recebe seus operandos, devolve o resultado e levanta exceções
em casos inválidos (divisão por zero, raiz de negativo, etc.). Nenhuma
função faz entrada ou saída de dados — isso fica a cargo do módulo ``cli``,
o que torna toda a lógica facilmente testável.
"""

from __future__ import annotations

import math

Numero = float


def soma(a: Numero, b: Numero) -> Numero:
    """Retorna a soma de ``a`` e ``b``."""
    return a + b


def subtracao(a: Numero, b: Numero) -> Numero:
    """Retorna a diferença entre ``a`` e ``b``."""
    return a - b


def multiplicacao(a: Numero, b: Numero) -> Numero:
    """Retorna o produto de ``a`` e ``b``."""
    return a * b


def divisao(a: Numero, b: Numero) -> Numero:
    """Retorna o quociente de ``a`` por ``b``.

    Raises:
        ZeroDivisionError: se ``b`` for igual a zero.
    """
    if b == 0:
        raise ZeroDivisionError("divisão por zero")
    return a / b


def potencia(base: Numero, expoente: Numero) -> Numero:
    """Retorna ``base`` elevado a ``expoente``."""
    return base ** expoente


def raiz_quadrada(x: Numero) -> Numero:
    """Retorna a raiz quadrada de ``x``.

    Raises:
        ValueError: se ``x`` for negativo.
    """
    if x < 0:
        raise ValueError("não existe raiz quadrada real de número negativo")
    return math.sqrt(x)


def resto(a: Numero, b: Numero) -> Numero:
    """Retorna o resto da divisão de ``a`` por ``b``.

    Raises:
        ZeroDivisionError: se ``b`` for igual a zero.
    """
    if b == 0:
        raise ZeroDivisionError("divisão por zero")
    return a % b


def porcentagem(valor: Numero, percentual: Numero) -> Numero:
    """Retorna ``percentual`` por cento de ``valor``."""
    return valor * percentual / 100


def valor_absoluto(x: Numero) -> Numero:
    """Retorna o valor absoluto de ``x``."""
    return abs(x)


def fatorial(n: int) -> int:
    """Retorna o fatorial de ``n``.

    Raises:
        ValueError: se ``n`` for negativo.
    """
    if n < 0:
        raise ValueError("o fatorial não é definido para números negativos")
    return math.factorial(n)


def maior(a: Numero, b: Numero) -> Numero:
    """Retorna o maior entre ``a`` e ``b``."""
    return max(a, b)


def menor(a: Numero, b: Numero) -> Numero:
    """Retorna o menor entre ``a`` e ``b``."""
    return min(a, b)


def media(a: Numero, b: Numero) -> Numero:
    """Retorna a média aritmética de ``a`` e ``b``."""
    return (a + b) / 2


def dobro(x: Numero) -> Numero:
    """Retorna o dobro de ``x``."""
    return x * 2


def triplo(x: Numero) -> Numero:
    """Retorna o triplo de ``x``."""
    return x * 3


def quadrado(x: Numero) -> Numero:
    """Retorna ``x`` ao quadrado."""
    return x ** 2


def cubo(x: Numero) -> Numero:
    """Retorna ``x`` ao cubo."""
    return x ** 3


def inverso(x: Numero) -> Numero:
    """Retorna o inverso multiplicativo de ``x`` (``1 / x``).

    Raises:
        ZeroDivisionError: se ``x`` for igual a zero.
    """
    if x == 0:
        raise ZeroDivisionError("não existe inverso de zero")
    return 1 / x


def eh_par(n: int) -> bool:
    """Retorna ``True`` se ``n`` for par e ``False`` caso contrário."""
    return n % 2 == 0


def comparar(a: Numero, b: Numero) -> int:
    """Compara ``a`` e ``b``.

    Returns:
        ``1`` se ``a > b``, ``-1`` se ``a < b`` e ``0`` se forem iguais.
    """
    if a > b:
        return 1
    if a < b:
        return -1
    return 0
