import math


def soma(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def multiplicacao(a, b):
    return a * b


def divisao(a, b):
    if b == 0:
        raise ZeroDivisionError("divisão por zero")
    return a / b


def potencia(base, expoente):
    return base ** expoente


def raiz_quadrada(x):
    if x < 0:
        raise ValueError("não existe raiz quadrada real de número negativo")
    return math.sqrt(x)


def resto(a, b):
    if b == 0:
        raise ZeroDivisionError("divisão por zero")
    return a % b


def porcentagem(valor, percentual):
    return valor * percentual / 100


def valor_absoluto(x):
    return abs(x)


def fatorial(n):
    if n < 0:
        raise ValueError("o fatorial não é definido para números negativos")
    return math.factorial(n)


def maior(a, b):
    return max(a, b)


def menor(a, b):
    return min(a, b)


def media(a, b):
    return (a + b) / 2


def dobro(x):
    return x * 2


def triplo(x):
    return x * 3


def quadrado(x):
    return x ** 2


def cubo(x):
    return x ** 3


def inverso(x):
    if x == 0:
        raise ZeroDivisionError("não existe inverso de zero")
    return 1 / x


def eh_par(n):
    return n % 2 == 0


def comparar(a, b):
    if a > b:
        return 1
    if a < b:
        return -1
    return 0
