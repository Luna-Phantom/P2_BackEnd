import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import app, Base, get_db, Produto

TEST_DATABASE_URL = "postgresql+psycopg://test_user:test_password@localhost:5433/test_db"

engine = create_engine(TEST_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="function")
def client():
    Base.metadata.create_all(bind=engine)
    
    def override_get_db():
        try:
            db = TestingSessionLocal()
            yield db
        finally:
            db.close()
            
    app.dependency_overrides[get_db] = override_get_db
    
    with TestClient(app) as c:
        yield c
        
    Base.metadata.drop_all(bind=engine)
    app.dependency_overrides.clear()

@pytest.fixture
def produto_existente(client):
    db = TestingSessionLocal()
    produto = Produto(nome="Brigadeiro Gourmet", preco=4.50, estoque=50, ativo=True)
    db.add(produto)
    db.commit()
    db.refresh(produto)
    db.close()
    return produto