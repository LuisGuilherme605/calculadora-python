# -*- coding: utf-8 -*-
"""Calculadora interativa com 20 operacoes matematicas."""

import math
import sys


def exibir_menu():
    """Exibe o menu de opcoes da calculadora."""
    print("Calculadora: essa calculadora tem as seguintes funcoes:\n")
    opcoes = [
        "Soma", "Subtracao", "Multiplicacao", "Divisao",
        "Potencia", "Raiz quadrada", "Resto", "Porcentagem",
        "Valor absoluto", "Fatorial", "Maior numero", "Menor numero",
        "Media", "Dobro", "Triplo", "Quadrado",
        "Cubo", "Inverso", "Par ou impar", "Ve qual o maior numero",
    ]
    for i, nome in enumerate(opcoes, start=1):
        print(f"{i} - {nome}")


def ler_float(prompt):
    """Le um numero decimal do usuario com validacao."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Erro: entrada invalida. Digite um numero.")


def ler_int(prompt):
    """Le um numero inteiro do usuario com validacao."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Erro: entrada invalida. Digite um numero inteiro.")


def soma():
    """Calcula a soma de dois numeros."""
    a = ler_float("Numero 1: ")
    b = ler_float("Numero 2: ")
    print(f"Resultado: {a + b}")


def subtracao():
    """Calcula a subtracao de dois numeros."""
    a = ler_float("Numero 1: ")
    b = ler_float("Numero 2: ")
    print(f"Resultado: {a - b}")


def multiplicacao():
    """Calcula a multiplicacao de dois numeros."""
    a = ler_float("Numero 1: ")
    b = ler_float("Numero 2: ")
    print(f"Resultado: {a * b}")


def divisao():
    """Calcula a divisao de dois numeros."""
    a = ler_float("Numero 1: ")
    b = ler_float("Numero 2: ")
    if b != 0:
        print(f"Resultado: {a / b}")
    else:
        print("Erro: divisao por zero.")


def potencia():
    """Calcula a potencia de um numero."""
    a = ler_float("Base: ")
    b = ler_float("Expoente: ")
    print(f"Resultado: {a ** b}")


def raiz_quadrada():
    """Calcula a raiz quadrada de um numero."""
    x = ler_float("Numero: ")
    if x >= 0:
        print(f"Resultado: {math.sqrt(x)}")
    else:
        print("Erro: numero negativo.")


def resto():
    """Calcula o resto da divisao de dois numeros."""
    a = ler_float("Numero 1: ")
    b = ler_float("Numero 2: ")
    if b != 0:
        print(f"Resultado: {a % b}")
    else:
        print("Erro: divisao por zero.")


def porcentagem():
    """Calcula a porcentagem de um valor."""
    a = ler_float("Valor: ")
    b = ler_float("Porcentagem: ")
    print(f"Resultado: {(a * b) / 100}")


def valor_absoluto():
    """Calcula o valor absoluto de um numero."""
    x = ler_float("Numero: ")
    print(f"Resultado: {abs(x)}")


def fatorial():
    """Calcula o fatorial de um numero inteiro."""
    x = ler_int("Numero: ")
    if x >= 0:
        print(f"Resultado: {math.factorial(x)}")
    else:
        print("Erro: numero negativo.")


def maior_numero():
    """Exibe o maior entre dois numeros."""
    a = ler_float("Numero 1: ")
    b = ler_float("Numero 2: ")
    print(f"Resultado: {max(a, b)}")


def menor_numero():
    """Exibe o menor entre dois numeros."""
    a = ler_float("Numero 1: ")
    b = ler_float("Numero 2: ")
    print(f"Resultado: {min(a, b)}")


def media():
    """Calcula a media de dois numeros."""
    a = ler_float("Numero 1: ")
    b = ler_float("Numero 2: ")
    print(f"Resultado: {(a + b) / 2}")


def dobro():
    """Calcula o dobro de um numero."""
    x = ler_float("Numero: ")
    print(f"Resultado: {x * 2}")


def triplo():
    """Calcula o triplo de um numero."""
    x = ler_float("Numero: ")
    print(f"Resultado: {x * 3}")


def quadrado():
    """Calcula o quadrado de um numero."""
    x = ler_float("Numero: ")
    print(f"Resultado: {x ** 2}")


def cubo():
    """Calcula o cubo de um numero."""
    x = ler_float("Numero: ")
    print(f"Resultado: {x ** 3}")


def inverso():
    """Calcula o inverso de um numero."""
    x = ler_float("Numero: ")
    if x != 0:
        print(f"Resultado: {1 / x}")
    else:
        print("Erro: divisao por zero.")


def par_ou_impar():
    """Verifica se um numero e par ou impar."""
    x = ler_int("Numero: ")
    if x % 2 == 0:
        print("Par")
    else:
        print("Impar")


def comparar_numeros():
    """Compara dois numeros e diz qual e maior."""
    a = ler_float("Numero 1: ")
    b = ler_float("Numero 2: ")
    if a > b:
        print("Primeiro maior")
    elif b > a:
        print("Segundo maior")
    else:
        print("Iguais")


OPERACOES = {
    1: soma,
    2: subtracao,
    3: multiplicacao,
    4: divisao,
    5: potencia,
    6: raiz_quadrada,
    7: resto,
    8: porcentagem,
    9: valor_absoluto,
    10: fatorial,
    11: maior_numero,
    12: menor_numero,
    13: media,
    14: dobro,
    15: triplo,
    16: quadrado,
    17: cubo,
    18: inverso,
    19: par_ou_impar,
    20: comparar_numeros,
}


def main():
    """Ponto de entrada principal da calculadora."""
    exibir_menu()
    try:
        opcao = int(input("\nEscolha uma opcao (1-20): "))
    except ValueError:
        print("Erro: opcao invalida. Digite um numero inteiro.")
        sys.exit(1)

    operacao = OPERACOES.get(opcao)
    if operacao:
        operacao()
    else:
        print("Opcao invalida. Escolha um numero de 1 a 20.")


if __name__ == "__main__":
    main()
