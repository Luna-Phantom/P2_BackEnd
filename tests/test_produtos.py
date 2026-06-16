import pytest

# 1. Listar produtos quando o banco está vazio
def test_listar_produtos_banco_vazio(client):
    response = client.get("/produtos")
    assert response.status_code == 200
    assert response.json() == []

# 2. Criar produto e verificar persistência no banco
def test_criar_produto_persistencia(client):
    payload = {"nome": "Bolo de Cenoura", "preco": 25.0, "estoque": 5}
    response = client.post("/produtos", json=payload)
    assert response.status_code == 201
    
    data = response.json()
    assert data["id"] is not None
    assert data["nome"] == "Bolo de Cenoura"

# 3. Criar produto e verificar que aparece na listagem
def test_criar_produto_aparece_na_listagem(client):
    client.post("/produtos", json={"nome": "Torta de Limão", "preco": 45.0})
    response = client.get("/produtos")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["nome"] == "Torta de Limão"

# 4. Buscar produto por id — caso de sucesso
def test_buscar_produto_por_id_sucesso(client, produto_existente):
    response = client.get(f"/produtos/{produto_existente.id}")
    assert response.status_code == 200
    assert response.json()["nome"] == "Brigadeiro Gourmet"

# 5. Buscar produto com id inexistente
def test_buscar_produto_id_inexistente(client):
    response = client.get("/produtos/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Produto não encontrado"

# 6. Deletar produto com sucesso
def test_deletar_produto_sucesso(client, produto_existente):
    response = client.delete(f"/produtos/{produto_existente.id}")
    assert response.status_code == 204

# 7. Deletar produto e confirmar remoção
def test_deletar_produto_confirmar_remocao(client, produto_existente):
    client.delete(f"/produtos/{produto_existente.id}")
    response = client.get(f"/produtos/{produto_existente.id}")
    assert response.status_code == 404

# 8. Deletar produto inexistente
def test_deletar_produto_inexistente(client):
    response = client.delete("/produtos/999")
    assert response.status_code == 404

# 9. Teste parametrizado cobrindo payloads inválidos
@pytest.mark.parametrize("payload_invalido", [
    {"nome": "", "preco": 10.0},         # Nome vazio
    {"nome": "Pudim", "preco": 0.0},     # Preço zero
    {"nome": "Cupcake", "preco": -5.0},  # Preço negativo
])
def test_criar_produto_payload_invalido(client, payload_invalido):
    response = client.post("/produtos", json=payload_invalido)
    assert response.status_code == 422

# 10. Validar que o banco está isolado
def test_validar_isolamento_do_banco(client):
    response = client.get("/produtos")
    assert response.status_code == 200
    assert response.json() == []