# Testes criados por Diego para CI 🚀

import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_hello_world(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.data.decode() == 'Hello, Docker!'

def test_test_no_params(client):
    response = client.get('/test')
    assert response.status_code == 400
    assert "Erro" in response.data.decode()

def test_test_with_params(client):
    response = client.get('/test?num=42&text=teste')
    assert response.status_code == 200
    assert 'Recebido número: 42 e texto: "teste"' in response.data.decode()
