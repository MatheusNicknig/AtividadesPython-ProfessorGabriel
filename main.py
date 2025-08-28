#Dupla: Matheus Nicknig e Marco Aurélio Moser

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Dict

app = FastAPI(
    title="API de Cadastro de Alunos",
    description="API para realizar as quatro operações básicas (CRUD) para alunos.",
    version="1.0.0"
)

# Modelo de dados do livro usando Pydantic
class Aluno(BaseModel):
    matricula: int
    nome: str
    turma: int
    idade: int

# "Banco de dados" em memória (um dicionário Python)
db_alunos: Dict[int, Aluno] = {
    1: Aluno(matricula="01", nome="Pedro Castro", turma=202, idade=17),
    2: Aluno(matricula="02", nome="Julia Tavares", turma=203, idade=15),
    3: Aluno(matricula="03", nome="Denilson Peres", turma=204, idade=16),
}

# --- ENDPOINTS DA API ---

@app.get("/")
def read_root():
    """Endpoint raiz da API."""
    return {"message": "Bem-vindo à API de Cadastro de alunos! Acesse /docs para a documentação interativa."}

@app.get("/alunos")
def pegar_todos_alunos():
    """Retorna todos os alunos cadastrados."""
    return db_alunos

@app.get("/alunos/{id}")
def pegar_alunos_por_id(id: int):
    """Retorna um alunos específico pelo seu Id."""
    if id not in db_alunos:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Aluno não encontrado")
    return db_alunos[id]

@app.post("/alunos/{id}", status_code=status.HTTP_201_CREATED)
def criar_alunos(id: int, aluno: Aluno):
    """Cria um novo aluno com um id específico."""
    if id in db_alunos:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Esse aluno já existe")

    db_alunos[id] = aluno
    return {"message": "Aluno cadastrado com sucesso!", "Id": id, "Aluno": Aluno}

@app.put("/alunos/{id}")
def atualizar_alunos(id: int, aluno: Aluno):
    """Atualiza as informações de um aluno existente."""
    if id not in db_alunos:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Aluno não encontrado")

    db_alunos [id] = aluno
    return {"message": "Cadastro do aluno atualizado com sucesso!", "Aluno": Aluno}

@app.delete("/alunos/{id}")
def deletar_alunos(id: int):
    """Deleta o cadastro de um aluno."""
    if id not in db_alunos:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Aluno não encontrado")

    del db_alunos[id]
    return {"message": "Aluno deletado com sucesso!"}