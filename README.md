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

## 💻 Comando exato para executar os testes
Com o banco de testes rodando, é só gerar o relatório de testes e cobertura com esse comando no terminal:

```bash
   pytest --cov=main -v

## 📊 Saída esperada do pytest

<img width="1919" height="1034" alt="image" src="https://github.com/user-attachments/assets/53894c78-cb24-4ce2-9282-1a6622e28576" />

## 🛡️ Explicação: Isolamento entre Testes
Como garantimos que um teste não bagunce o resultado do outro? Usando a fixture `client` no arquivo `conftest.py`. Ela faz o ciclo completo:

1. **`create_all`**: Cria as tabelas do zero no banco de testes.
2. **`dependency_overrides`**: Força a API a usar o banco de testes em vez do banco principal.
3. **`yield`**: Libera o teste específico para rodar.
4. **`drop_all`**: Logo que o teste acaba, ela apaga tudo. Assim, o próximo teste sempre pega o banco zerado e sem sujeira.
