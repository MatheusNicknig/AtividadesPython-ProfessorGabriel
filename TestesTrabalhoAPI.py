import pytest
from fastapi.testclient import TestClient
from TrabalhoAPI import app, db_tarefas


client = TestClient(app)


@pytest.fixture(autouse=True)
def limpar_db():
    """Limpa o banco antes de cada teste."""
    db_tarefas.clear()
    yield
    db_tarefas.clear()


# ============ CRIAÇÃO DE TAREFA ============

def test_criar_tarefa_sucesso():
    """Testa criação bem-sucedida de uma tarefa."""
    response = client.post("/tarefas", json={
        "titulo": "Estudar Python"
    })
    assert response.status_code == 201
    assert response.json()["titulo"] == "Estudar Python"


def test_criar_tarefa_sem_titulo():
    """Testa falha na criação sem o campo título."""
    response = client.post("/tarefas", json={})
    assert response.status_code == 422


# ============ LISTAGEM DE TAREFAS ============

def test_listar_tarefas_vazio():
    """Testa listagem com zero tarefas."""
    response = client.get("/tarefas")
    assert response.status_code == 200
    assert len(response.json()) == 0


def test_listar_tarefas_com_multiplas():
    """Testa listagem com múltiplas tarefas."""
    client.post("/tarefas", json={"titulo": "Tarefa 1"})
    client.post("/tarefas", json={"titulo": "Tarefa 2"})
    
    response = client.get("/tarefas")
    assert response.status_code == 200
    assert len(response.json()) == 2


# ============ BUSCA POR ID ============

def test_obter_tarefa_id_valido():
    """Testa busca por ID existente."""
    create_response = client.post("/tarefas", json={"titulo": "Minha Tarefa"})
    tarefa_id = create_response.json()["id"]
    
    response = client.get(f"/tarefas/{tarefa_id}")
    assert response.status_code == 200
    assert response.json()["titulo"] == "Minha Tarefa"


def test_obter_tarefa_id_inexistente():
    """Testa busca por ID que não existe."""
    response = client.get("/tarefas/id-inexistente")
    assert response.status_code == 404


# ============ ATUALIZAÇÃO DE TAREFA ============

def test_atualizar_tarefa_sucesso():
    """Testa atualização bem-sucedida de uma tarefa."""
    create_response = client.post("/tarefas", json={"titulo": "Original"})
    tarefa_id = create_response.json()["id"]
    
    response = client.put(f"/tarefas/{tarefa_id}", json={"titulo": "Atualizado"})
    assert response.status_code == 200
    assert response.json()["titulo"] == "Atualizado"


def test_atualizar_tarefa_id_inexistente():
    """Testa atualização com ID inexistente."""
    response = client.put("/tarefas/id-inexistente", json={"titulo": "Novo"})
    assert response.status_code == 404


# ============ DELEÇÃO DE TAREFA ============

def test_deletar_tarefa_sucesso():
    """Testa deleção bem-sucedida de uma tarefa."""
    create_response = client.post("/tarefas", json={"titulo": "A Deletar"})
    tarefa_id = create_response.json()["id"]
    
    response = client.delete(f"/tarefas/{tarefa_id}")
    assert response.status_code == 204


def test_deletar_tarefa_depois_nao_existe():
    """Testa se após deleção a tarefa realmente desaparece."""
    create_response = client.post("/tarefas", json={"titulo": "A Deletar"})
    tarefa_id = create_response.json()["id"]
    
    client.delete(f"/tarefas/{tarefa_id}")
    
    response = client.get(f"/tarefas/{tarefa_id}")
    assert response.status_code == 404


def test_deletar_tarefa_id_inexistente():
    """Testa deleção com ID inexistente."""
    response = client.delete("/tarefas/id-inexistente")
    assert response.status_code == 404
