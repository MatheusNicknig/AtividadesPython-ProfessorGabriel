import pytest
from fastapi.testclient import TestClient
from api_tarefas import app, db_tarefas

# Criar cliente de teste
client = TestClient(app)

# Fixture para limpar o banco de dados antes de cada teste
@pytest.fixture(autouse=True)
def limpar_db():
    """Limpa o banco de dados em memória antes de cada teste."""
    db_tarefas.clear()
    yield
    db_tarefas.clear()

# ============================================
# TESTES DE CRIAÇÃO DE TAREFA
# ============================================

def test_criar_tarefa_sucesso():
    """Testa a criação bem-sucedida de uma tarefa."""
    response = client.post("/tarefas", json={
        "titulo": "Estudar Python",
        "descricao": "Aprender conceitos de FastAPI"
    })
    
    assert response.status_code == 201
    data = response.json()
    assert data["titulo"] == "Estudar Python"
    assert data["descricao"] == "Aprender conceitos de FastAPI"
    assert data["concluida"] == False
    assert "id" in data


def test_criar_tarefa_sem_titulo():
    """Testa falha na criação por falta do campo título."""
    response = client.post("/tarefas", json={
        "descricao": "Descrição sem título"
    })
    
    assert response.status_code == 422


def test_criar_tarefa_titulo_muito_curto():
    """Testa falha na criação com título muito curto (menos de 3 caracteres)."""
    response = client.post("/tarefas", json={
        "titulo": "ab"
    })
    
    assert response.status_code == 422


def test_criar_tarefa_com_descricao_opcional():
    """Testa criação de tarefa com descricao opcional."""
    response = client.post("/tarefas", json={
        "titulo": "Tarefa sem descrição"
    })
    
    assert response.status_code == 201
    data = response.json()
    assert data["descricao"] is None


def test_criar_tarefa_com_concluida():
    """Testa criação de tarefa com status de conclusão."""
    response = client.post("/tarefas", json={
        "titulo": "Tarefa já concluída",
        "concluida": True
    })
    
    assert response.status_code == 201
    data = response.json()
    assert data["concluida"] == True


def test_id_gerado_automaticamente():
    """Testa se o ID é gerado automaticamente e é único."""
    response1 = client.post("/tarefas", json={"titulo": "Tarefa 1"})
    response2 = client.post("/tarefas", json={"titulo": "Tarefa 2"})
    
    id1 = response1.json()["id"]
    id2 = response2.json()["id"]
    
    assert id1 != id2
    assert len(id1) > 0
    assert len(id2) > 0


# ============================================
# TESTES DE LISTAGEM DE TAREFAS
# ============================================

def test_listar_tarefas_vazio():
    """Testa listagem quando não há nenhuma tarefa."""
    response = client.get("/tarefas")
    
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 0


def test_listar_tarefas_com_uma_tarefa():
    """Testa listagem com uma tarefa."""
    # Criar uma tarefa
    client.post("/tarefas", json={"titulo": "Tarefa 1"})
    
    # Listar tarefas
    response = client.get("/tarefas")
    
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["titulo"] == "Tarefa 1"


def test_listar_tarefas_com_multiplas_tarefas():
    """Testa listagem quando existem múltiplas tarefas."""
    # Criar múltiplas tarefas
    for i in range(3):
        client.post("/tarefas", json={
            "titulo": f"Tarefa {i+1}",
            "descricao": f"Descrição {i+1}"
        })
    
    # Listar tarefas
    response = client.get("/tarefas")
    
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 3


# ============================================
# TESTES DE BUSCA POR ID
# ============================================

def test_obter_tarefa_por_id_valido():
    """Testa busca por um ID válido e existente."""
    # Criar uma tarefa
    create_response = client.post("/tarefas", json={
        "titulo": "Tarefa Teste",
        "descricao": "Descrição teste"
    })
    tarefa_id = create_response.json()["id"]
    
    # Obter a tarefa
    response = client.get(f"/tarefas/{tarefa_id}")
    
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == tarefa_id
    assert data["titulo"] == "Tarefa Teste"
    assert data["descricao"] == "Descrição teste"


def test_obter_tarefa_por_id_inexistente():
    """Testa busca por um ID que não existe."""
    response = client.get("/tarefas/id-inexistente-12345")
    
    assert response.status_code == 404
    data = response.json()
    assert "detail" in data


# ============================================
# TESTES DE ATUALIZAÇÃO DE TAREFA
# ============================================

def test_atualizar_tarefa_sucesso():
    """Testa atualização bem-sucedida de uma tarefa."""
    # Criar uma tarefa
    create_response = client.post("/tarefas", json={
        "titulo": "Tarefa Original",
        "descricao": "Descrição original",
        "concluida": False
    })
    tarefa_id = create_response.json()["id"]
    
    # Atualizar a tarefa
    response = client.put(f"/tarefas/{tarefa_id}", json={
        "titulo": "Tarefa Atualizada",
        "descricao": "Descrição atualizada",
        "concluida": True
    })
    
    assert response.status_code == 200
    data = response.json()
    assert data["titulo"] == "Tarefa Atualizada"
    assert data["descricao"] == "Descrição atualizada"
    assert data["concluida"] == True


def test_atualizar_apenas_titulo():
    """Testa atualização de apenas o título."""
    # Criar uma tarefa
    create_response = client.post("/tarefas", json={
        "titulo": "Tarefa Original",
        "descricao": "Descrição original"
    })
    tarefa_id = create_response.json()["id"]
    
    # Atualizar apenas o título
    response = client.put(f"/tarefas/{tarefa_id}", json={
        "titulo": "Novo Título"
    })
    
    assert response.status_code == 200
    data = response.json()
    assert data["titulo"] == "Novo Título"
    assert data["descricao"] == "Descrição original"


def test_atualizar_apenas_concluida():
    """Testa atualização de apenas o status de conclusão."""
    # Criar uma tarefa
    create_response = client.post("/tarefas", json={
        "titulo": "Tarefa",
        "concluida": False
    })
    tarefa_id = create_response.json()["id"]
    
    # Atualizar apenas o status
    response = client.put(f"/tarefas/{tarefa_id}", json={
        "concluida": True
    })
    
    assert response.status_code == 200
    data = response.json()
    assert data["concluida"] == True


def test_atualizar_tarefa_id_inexistente():
    """Testa tentativa de atualizar uma tarefa com ID inexistente."""
    response = client.put("/tarefas/id-inexistente-12345", json={
        "titulo": "Nova Tarefa"
    })
    
    assert response.status_code == 404


def test_atualizar_tarefa_titulo_muito_curto():
    """Testa tentativa de atualizar com título muito curto."""
    # Criar uma tarefa
    create_response = client.post("/tarefas", json={
        "titulo": "Tarefa Original"
    })
    tarefa_id = create_response.json()["id"]
    
    # Tentar atualizar com título inválido
    response = client.put(f"/tarefas/{tarefa_id}", json={
        "titulo": "ab"
    })
    
    assert response.status_code == 422


# ============================================
# TESTES DE DELEÇÃO DE TAREFA
# ============================================

def test_deletar_tarefa_sucesso():
    """Testa deleção bem-sucedida de uma tarefa."""
    # Criar uma tarefa
    create_response = client.post("/tarefas", json={
        "titulo": "Tarefa a Deletar"
    })
    tarefa_id = create_response.json()["id"]
    
    # Deletar a tarefa
    response = client.delete(f"/tarefas/{tarefa_id}")
    
    assert response.status_code == 204


def test_deletar_tarefa_verificar_nao_existe():
    """Testa se após deleção uma nova busca resulta em erro 404."""
    # Criar uma tarefa
    create_response = client.post("/tarefas", json={
        "titulo": "Tarefa a Deletar"
    })
    tarefa_id = create_response.json()["id"]
    
    # Deletar a tarefa
    delete_response = client.delete(f"/tarefas/{tarefa_id}")
    assert delete_response.status_code == 204
    
    # Tentar obter a tarefa deletada
    get_response = client.get(f"/tarefas/{tarefa_id}")
    assert get_response.status_code == 404


def test_deletar_tarefa_id_inexistente():
    """Testa tentativa de deletar uma tarefa com ID inexistente."""
    response = client.delete("/tarefas/id-inexistente-12345")
    
    assert response.status_code == 404


def test_deletar_tarefa_nao_afeta_outras():
    """Testa se deletar uma tarefa não afeta outras."""
    # Criar duas tarefas
    response1 = client.post("/tarefas", json={"titulo": "Tarefa 1"})
    response2 = client.post("/tarefas", json={"titulo": "Tarefa 2"})
    
    id1 = response1.json()["id"]
    id2 = response2.json()["id"]
    
    # Deletar a primeira tarefa
    client.delete(f"/tarefas/{id1}")
    
    # Verificar que a segunda tarefa ainda existe
    response = client.get(f"/tarefas/{id2}")
    assert response.status_code == 200
    
    # Verificar listagem
    list_response = client.get("/tarefas")
    assert len(list_response.json()) == 1
    assert list_response.json()[0]["id"] == id2


# ============================================
# TESTES DE INTEGRAÇÃO
# ============================================

def test_fluxo_completo():
    """Testa um fluxo completo de operações."""
    # Criar tarefa
    create_response = client.post("/tarefas", json={
        "titulo": "Aprender FastAPI",
        "descricao": "Criar uma API RESTful"
    })
    assert create_response.status_code == 201
    tarefa_id = create_response.json()["id"]
    
    # Listar tarefas
    list_response = client.get("/tarefas")
    assert list_response.status_code == 200
    assert len(list_response.json()) == 1
    
    # Obter tarefa específica
    get_response = client.get(f"/tarefas/{tarefa_id}")
    assert get_response.status_code == 200
    assert get_response.json()["titulo"] == "Aprender FastAPI"
    
    # Atualizar tarefa
    update_response = client.put(f"/tarefas/{tarefa_id}", json={
        "concluida": True
    })
    assert update_response.status_code == 200
    assert update_response.json()["concluida"] == True
    
    # Deletar tarefa
    delete_response = client.delete(f"/tarefas/{tarefa_id}")
    assert delete_response.status_code == 204
    
    # Verificar que foi deletada
    list_response = client.get("/tarefas")
    assert len(list_response.json()) == 0


def test_multiplas_tarefas_operacoes():
    """Testa operações com múltiplas tarefas."""
    ids = []
    
    # Criar 5 tarefas
    for i in range(5):
        response = client.post("/tarefas", json={
            "titulo": f"Tarefa {i+1}",
            "descricao": f"Descrição {i+1}"
        })
        ids.append(response.json()["id"])
    
    # Verificar listagem
    list_response = client.get("/tarefas")
    assert len(list_response.json()) == 5
    
    # Atualizar algumas tarefas
    client.put(f"/tarefas/{ids[0]}", json={"concluida": True})
    client.put(f"/tarefas/{ids[2]}", json={"concluida": True})
    
    # Deletar uma tarefa
    client.delete(f"/tarefas/{ids[1]}")
    
    # Verificar estado final
    list_response = client.get("/tarefas")
    assert len(list_response.json()) == 4
    
    # Verificar que as tarefas certas foram marcadas como concluídas
    assert client.get(f"/tarefas/{ids[0]}").json()["concluida"] == True
    assert client.get(f"/tarefas/{ids[2]}").json()["concluida"] == True