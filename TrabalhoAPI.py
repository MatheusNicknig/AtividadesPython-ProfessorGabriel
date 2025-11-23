from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import Dict, Optional
import uuid

app = FastAPI(
    title="API de Gerenciamento de Tarefas",
    description="API RESTful para gerenciar uma lista de tarefas (To-Do List)",
    version="1.0.0"
)

# Modelo de dados da Tarefa usando Pydantic
class Tarefa(BaseModel):
    titulo: str = Field(..., min_length=3, description="Título da tarefa (mínimo 3 caracteres)")
    descricao: Optional[str] = Field(default=None, description="Descrição detalhada da tarefa")
    concluida: bool = Field(default=False, description="Status de conclusão da tarefa")

# Modelo para atualização de tarefa
class TarefaUpdate(BaseModel):
    titulo: Optional[str] = Field(None, min_length=3)
    descricao: Optional[str] = None
    concluida: Optional[bool] = None

# "Banco de dados" em memória (um dicionário Python)
db_tarefas: Dict[str, Tarefa] = {}

# --- ENDPOINTS DA API ---

@app.get("/")
def read_root():
    """Endpoint raiz da API."""
    return {"message": "Bem-vindo à API de Gerenciamento de Tarefas! Acesse /docs para a documentação interativa."}

@app.get("/tarefas", status_code=status.HTTP_200_OK)
def listar_todas_tarefas():
    """Retorna todas as tarefas cadastradas."""
    return list(db_tarefas.values())

@app.get("/tarefas/{id}", status_code=status.HTTP_200_OK)
def obter_tarefa_por_id(id: str):
    """Retorna uma tarefa específica pelo seu ID."""
    if id not in db_tarefas:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Tarefa não encontrada"
        )
    return db_tarefas[id]

@app.post("/tarefas", status_code=status.HTTP_201_CREATED)
def criar_tarefa(tarefa_data: Tarefa):
    idDaTarefa = str(uuid.uuid4())
    """Cria uma nova tarefa com ID gerado automaticamente."""
    tarefa = Tarefa(
        titulo=tarefa_data.titulo,
        descricao=tarefa_data.descricao,
        concluida=tarefa_data.concluida
    )
    
    db_tarefas[idDaTarefa] = tarefa
    return tarefa

@app.put("/tarefas/{id}", status_code=status.HTTP_200_OK)
def atualizar_tarefa(id: str, tarefa_update: TarefaUpdate):
    """Atualiza as informações de uma tarefa existente."""
    if id not in db_tarefas:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Tarefa não encontrada"
        )
    
    tarefa_existente = db_tarefas[id]
    
    # Atualizar apenas os campos fornecidos
    if tarefa_update.titulo is not None:
        tarefa_existente.titulo = tarefa_update.titulo
    if tarefa_update.descricao is not None:
        tarefa_existente.descricao = tarefa_update.descricao
    if tarefa_update.concluida is not None:
        tarefa_existente.concluida = tarefa_update.concluida
    
    db_tarefas[id] = tarefa_existente
    return db_tarefas[id]

@app.delete("/tarefas/{id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_tarefa(id: str):
    """Deleta uma tarefa existente."""
    if id not in db_tarefas:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Tarefa não encontrada"
        )
    
    del db_tarefas[id]
    return None