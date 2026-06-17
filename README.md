# Calculadora em Python

Uma calculadora de linha de comando que fiz pra praticar Python. Tem 20 operações
(as básicas e mais umas como fatorial, porcentagem, média) e roda num menu no
terminal: você escolhe a operação, digita os números e ela mostra o resultado.

Separei a parte das contas (`operacoes.py`) da parte que fala com o usuário
(`cli.py`) porque assim dá pra testar as contas sem ficar digitando no terminal.

## Como rodar

Precisa de Python 3.9 ou mais novo.

```bash
git clone https://github.com/LuisGuilherme605/calculadora-python.git
cd calculadora-python
pip install -e .
calculadora
```

Ou, sem instalar nada:

```bash
python -m calculadora.cli
```

## Operações

soma, subtração, multiplicação, divisão, potência, raiz quadrada, resto da divisão,
porcentagem, valor absoluto, fatorial, maior, menor, média, dobro, triplo, quadrado,
cubo, inverso, par ou ímpar e comparar dois números.

No menu é só digitar o número da operação. Pra sair, digita 0.

## Testes

Tem alguns testes com pytest pra conferir as contas:

```bash
pip install -e ".[dev]"
pytest
```
