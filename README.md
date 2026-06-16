# Atividade: E-commerce de Doces - API com FastAPI e Pytest

## Descrição
API feita com FastAPI para gerenciar os produtos de uma doceria. O projeto tem testes automatizados feitos com Pytest que rodam contra um banco PostgreSQL de verdade, usando Docker para garantir o isolamento.

## 🚀 Tecnologias Utilizadas
* **Python (FastAPI):** 
* **SQLAlchemy & Pydantic:** 
* **PostgreSQL:** 
* **Pytest:** 
* **Docker & Docker Compose:** 

## Instruções para subir o banco de teste com Docker
Para garantir que os testes rodem num ambiente limpo, a gente sobe a infraestrutura pelo Docker Compose:

1. Confirme se o Docker está rodando no seu computador.
2. No terminal, na pasta raiz do projeto, rode o comando:
   ```bash
   docker-compose up -d db_test

Comando exato para executar os testes

pytest --cov=main -v

Saída esperada do pytest

============================= test session starts ==============================
collected 12 items

tests/test_produtos.py::test_listar_produtos_banco_vazio PASSED          [  8%]
tests/test_produtos.py::test_criar_produto_persistencia PASSED           [ 16%]
tests/test_produtos.py::test_criar_produto_aparece_na_listagem PASSED    [ 25%]
tests/test_produtos.py::test_buscar_produto_por_id_sucesso PASSED        [ 33%]
tests/test_produtos.py::test_buscar_produto_id_inexistente PASSED        [ 41%]
tests/test_produtos.py::test_deletar_produto_sucesso PASSED              [ 50%]
tests/test_produtos.py::test_deletar_produto_confirmar_remocao PASSED    [ 58%]
tests/test_produtos.py::test_deletar_produto_inexistente PASSED          [ 66%]
tests/test_produtos.py::test_criar_produto_payload_invalido[payload_invalido0] PASSED [ 75%]
tests/test_produtos.py::test_criar_produto_payload_invalido[payload_invalido1] PASSED [ 83%]
tests/test_produtos.py::test_criar_produto_payload_invalido[payload_invalido2] PASSED [ 91%]
tests/test_produtos.py::test_validar_isolamento_do_banco PASSED          [100%]

---------- coverage: platform win32, python 3.13.14-final-0 -----------
Name      Stmts   Miss  Cover
-----------------------------
main.py      56      4    93%
-----------------------------
TOTAL        56      4    93%

======================== 12 passed, 2 warnings in 0.78s ========================

Explicação: Isolamento entre Testes
Como garantimos que um teste não bagunce o resultado do outro? Usando a fixture client no arquivo conftest.py. Ela faz o ciclo completo:

- create_all: Cria as tabelas do zero no banco de testes.
- dependency_overrides: Força a API a usar o banco de testes em vez do banco principal.
- yield: Libera o teste específico para rodar.
- drop_all: Logo que o teste acaba, ela apaga tudo. Assim, o próximo teste sempre pega o banco zerado e sem sujeira.