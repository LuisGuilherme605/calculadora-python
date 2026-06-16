# Calculadora Python

[![CI](https://github.com/LuisGuilherme605/calculadora-python/actions/workflows/ci.yml/badge.svg)](https://github.com/LuisGuilherme605/calculadora-python/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Calculadora interativa de linha de comando com **20 operações matemáticas**.
O projeto separa a lógica matemática da interface com o usuário, possui testes
automatizados e integração contínua — uma base simples, porém organizada nos
moldes de projetos profissionais em Python.

## Funcionalidades

| #  | Operação          | #  | Operação                |
|----|-------------------|----|-------------------------|
| 1  | Soma              | 11 | Maior número            |
| 2  | Subtração         | 12 | Menor número            |
| 3  | Multiplicação     | 13 | Média                   |
| 4  | Divisão           | 14 | Dobro                   |
| 5  | Potência          | 15 | Triplo                  |
| 6  | Raiz quadrada     | 16 | Quadrado                |
| 7  | Resto da divisão  | 17 | Cubo                    |
| 8  | Porcentagem       | 18 | Inverso                 |
| 9  | Valor absoluto    | 19 | Par ou ímpar            |
| 10 | Fatorial          | 20 | Comparar dois números   |

O menu roda em laço: após cada cálculo é possível escolher outra operação ou
digitar `0` para sair.

## Instalação e execução

Pré-requisito: [Python 3.9+](https://www.python.org/downloads/).

```bash
# 1. Clone o repositório
git clone https://github.com/LuisGuilherme605/calculadora-python.git
cd calculadora-python

# 2. (Opcional) crie um ambiente virtual
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 3. Instale o projeto
pip install -e .

# 4. Execute
calculadora                       # via comando instalado
# ou
python -m calculadora.cli         # sem instalar
```

## Desenvolvimento

Instale as dependências de desenvolvimento e rode os testes e o linter:

```bash
pip install -e ".[dev]"
pytest          # executa a suíte de testes
ruff check .    # verifica o estilo do código
```

## Estrutura do projeto

```
calculadora-python/
├── .github/workflows/ci.yml      # Integração contínua (testes + lint)
├── src/calculadora/
│   ├── __init__.py
│   ├── operacoes.py              # Lógica matemática pura (testável)
│   └── cli.py                    # Interface de linha de comando
├── tests/
│   └── test_operacoes.py         # Testes unitários
├── pyproject.toml                # Configuração e metadados do projeto
├── LICENSE                       # Licença MIT
├── CONTRIBUTING.md               # Guia de contribuição
└── README.md
```

## Tecnologias

- **Python 3.9+** — linguagem de programação
- **pytest** — testes automatizados
- **ruff** — linter e formatador
- **GitHub Actions** — integração contínua

## Licença

Distribuído sob a licença [MIT](LICENSE).
