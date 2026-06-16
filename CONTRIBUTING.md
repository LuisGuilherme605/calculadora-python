# Guia de Contribuição

Obrigado pelo interesse em contribuir! Siga os passos abaixo para manter o
projeto consistente e organizado.

## Ambiente de desenvolvimento

```bash
git clone https://github.com/LuisGuilherme605/calculadora-python.git
cd calculadora-python
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
```

## Fluxo de trabalho

1. Crie uma branch a partir da `main`:
   ```bash
   git checkout -b minha-feature
   ```
2. Faça suas alterações mantendo o estilo do código existente.
3. Garanta que tudo está verde antes de abrir o Pull Request:
   ```bash
   ruff check .
   pytest
   ```
4. Escreva mensagens de commit claras e descritivas.
5. Abra um Pull Request descrevendo a motivação e o que foi alterado.

## Padrões de código

- Toda nova operação matemática deve ser adicionada em `src/calculadora/operacoes.py`
  como uma função pura (sem entrada/saída) e acompanhada de testes em
  `tests/test_operacoes.py`.
- A interação com o usuário pertence apenas a `src/calculadora/cli.py`.
- Mantenha o código tipado e documentado com docstrings.
