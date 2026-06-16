# Atividade: E-commerce de Doces - API com FastAPI e Pytest

## Descrição
API feita com FastAPI para gerenciar os produtos de uma doceria. O projeto tem testes automatizados feitos com Pytest que rodam contra um banco PostgreSQL de verdade, usando Docker para garantir o isolamento.

## 🚀 Tecnologias Utilizadas
* **Python (FastAPI):** 
* **SQLAlchemy & Pydantic:** 
* **PostgreSQL:** 
* **Pytest:** 
* **Docker & Docker Compose:**

## 🛠️ Preparação do Ambiente
Antes de rodar a API ou os testes, configure o ambiente virtual e instale as dependências:

1. **Crie e ative o ambiente virtual:**
   ```bash
   python -m venv venv
   .\venv\Scripts\Activate.ps1

## Instale as dependências
   ```bash
   pip install -r requirements.txt
   ```

## 🐳 Instruções de Infraestrutura (Docker)
O projeto utiliza dois bancos de dados via Docker para separar o ambiente de desenvolvimento do ambiente de testes(Lembre-se de certificar que o programa Docker está aberto em sua máquina):

* **Para rodar o ambiente de desenvolvimento:**
  ```bash
  docker-compose up -d db_dev
   ```
**Para rodar o ambiente de testes:**
   ```bash
   docker-compose up -d db_test
   ```

## 💻 Comando exato para executar os testes
Com o banco de testes rodando, é só gerar o relatório de testes e cobertura com esse comando no terminal:

```bash
pytest --cov=main -v
```

## 📊 Saída esperada do pytest

<img width="1919" height="1034" alt="image" src="https://github.com/user-attachments/assets/53894c78-cb24-4ce2-9282-1a6622e28576" />

## 🛡️ Explicação: Isolamento entre Testes
Como garantimos que um teste não bagunce o resultado do outro? Usando a fixture `client` no arquivo `conftest.py`. Ela faz o ciclo completo:

1. **`create_all`**: Cria as tabelas do zero no banco de testes.
2. **`dependency_overrides`**: Força a API a usar o banco de testes em vez do banco principal.
3. **`yield`**: Libera o teste específico para rodar.
4. **`drop_all`**: Logo que o teste acaba, ela apaga tudo. Assim, o próximo teste sempre pega o banco zerado e sem sujeira.
