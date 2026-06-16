"""Interface de linha de comando da calculadora.

Responsável por toda a interação com o usuário: exibição do menu, leitura
e validação das entradas e apresentação dos resultados. A lógica matemática
fica isolada no módulo :mod:`calculadora.operacoes`.
"""

from __future__ import annotations

from collections.abc import Callable

from calculadora import operacoes


def ler_float(prompt: str) -> float:
    """Lê um número decimal do usuário, repetindo até a entrada ser válida."""
    while True:
        try:
            return float(input(prompt).replace(",", "."))
        except ValueError:
            print("Entrada inválida. Digite um número.")


def ler_int(prompt: str) -> int:
    """Lê um número inteiro do usuário, repetindo até a entrada ser válida."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")


def _binaria(funcao: Callable[[float, float], float], unidade: str = "") -> None:
    """Executa uma operação que recebe dois números decimais."""
    a = ler_float("Número 1: ")
    b = ler_float("Número 2: ")
    print(f"Resultado: {funcao(a, b)}{unidade}")


def _unaria(funcao: Callable[[float], float]) -> None:
    """Executa uma operação que recebe um único número decimal."""
    x = ler_float("Número: ")
    print(f"Resultado: {funcao(x)}")


def _divisao() -> None:
    a = ler_float("Número 1: ")
    b = ler_float("Número 2: ")
    try:
        print(f"Resultado: {operacoes.divisao(a, b)}")
    except ZeroDivisionError:
        print("Erro: não é possível dividir por zero.")


def _resto() -> None:
    a = ler_float("Número 1: ")
    b = ler_float("Número 2: ")
    try:
        print(f"Resultado: {operacoes.resto(a, b)}")
    except ZeroDivisionError:
        print("Erro: não é possível dividir por zero.")


def _raiz_quadrada() -> None:
    x = ler_float("Número: ")
    try:
        print(f"Resultado: {operacoes.raiz_quadrada(x)}")
    except ValueError as erro:
        print(f"Erro: {erro}.")


def _inverso() -> None:
    x = ler_float("Número: ")
    try:
        print(f"Resultado: {operacoes.inverso(x)}")
    except ZeroDivisionError:
        print("Erro: não existe inverso de zero.")


def _fatorial() -> None:
    n = ler_int("Número: ")
    try:
        print(f"Resultado: {operacoes.fatorial(n)}")
    except ValueError as erro:
        print(f"Erro: {erro}.")


def _par_ou_impar() -> None:
    n = ler_int("Número: ")
    print("Par" if operacoes.eh_par(n) else "Ímpar")


def _comparar() -> None:
    a = ler_float("Número 1: ")
    b = ler_float("Número 2: ")
    resultado = operacoes.comparar(a, b)
    if resultado > 0:
        print("O primeiro número é maior.")
    elif resultado < 0:
        print("O segundo número é maior.")
    else:
        print("Os números são iguais.")


# Cada item do menu: (rótulo, ação a executar).
MENU: dict[int, tuple[str, Callable[[], None]]] = {
    1: ("Soma", lambda: _binaria(operacoes.soma)),
    2: ("Subtração", lambda: _binaria(operacoes.subtracao)),
    3: ("Multiplicação", lambda: _binaria(operacoes.multiplicacao)),
    4: ("Divisão", _divisao),
    5: ("Potência", lambda: _binaria(operacoes.potencia)),
    6: ("Raiz quadrada", _raiz_quadrada),
    7: ("Resto da divisão", _resto),
    8: ("Porcentagem", lambda: _binaria(operacoes.porcentagem)),
    9: ("Valor absoluto", lambda: _unaria(operacoes.valor_absoluto)),
    10: ("Fatorial", _fatorial),
    11: ("Maior número", lambda: _binaria(operacoes.maior)),
    12: ("Menor número", lambda: _binaria(operacoes.menor)),
    13: ("Média", lambda: _binaria(operacoes.media)),
    14: ("Dobro", lambda: _unaria(operacoes.dobro)),
    15: ("Triplo", lambda: _unaria(operacoes.triplo)),
    16: ("Quadrado", lambda: _unaria(operacoes.quadrado)),
    17: ("Cubo", lambda: _unaria(operacoes.cubo)),
    18: ("Inverso", _inverso),
    19: ("Par ou ímpar", _par_ou_impar),
    20: ("Comparar dois números", _comparar),
}


def exibir_menu() -> None:
    """Imprime o menu de operações disponíveis."""
    print("\n=== Calculadora ===")
    metade = (len(MENU) + 1) // 2
    for i in range(1, metade + 1):
        esquerda = f"{i:>2} - {MENU[i][0]}"
        indice_direito = i + metade
        if indice_direito in MENU:
            direita = f"{indice_direito:>2} - {MENU[indice_direito][0]}"
            print(f"{esquerda:<28}{direita}")
        else:
            print(esquerda)
    print(" 0 - Sair")


def executar() -> None:
    """Laço principal interativo da calculadora."""
    while True:
        exibir_menu()
        try:
            opcao = int(input("\nEscolha uma opção: "))
        except ValueError:
            print("Opção inválida. Digite um número.")
            continue

        if opcao == 0:
            print("Encerrando. Até logo!")
            break

        item = MENU.get(opcao)
        if item is None:
            print("Opção inválida. Escolha um número do menu.")
            continue

        _, acao = item
        acao()


def main() -> None:
    """Ponto de entrada que trata interrupção pelo teclado."""
    try:
        executar()
    except (KeyboardInterrupt, EOFError):
        print("\nEncerrando. Até logo!")


if __name__ == "__main__":
    main()
