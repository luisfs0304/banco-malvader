from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import SessionLocal, engine, Base
import pyotp
import datetime
from datetime import date

# Criar as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Banco Malvader API")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API do Banco Malvader!"}

# Rota para criar primeiro usuário (apenas para desenvolvimento)
@app.post("/primeiro-usuario/")
def criar_primeiro_usuario(db: Session = Depends(get_db)):
    # Verificar se já existe algum usuário
    if db.query(models.Usuario).first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Já existe um usuário no sistema"
        )
    
    # Criar usuário admin
    otp_secret = pyotp.random_base32()
    senha_hash = crud.get_password_hash("admin123")
    
    db_usuario = models.Usuario(
        login="admin",
        senha=senha_hash,
        nome="Administrador",
        otp_secret=otp_secret
    )
    
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    
    return {
        "message": "Usuário admin criado com sucesso",
        "login": "admin",
        "senha": "admin123",
        "otp_secret": otp_secret
    }

# Rotas de Autenticação
@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = crud.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuário ou senha incorretos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Gerar OTP
    otp = pyotp.TOTP(user.otp_secret)
    current_otp = otp.now()
    
    return {
        "access_token": "dummy_token",  # Em produção, use JWT
        "token_type": "bearer",
        "otp": current_otp
    }

# Rotas de Agência
@app.get("/agencias/", response_model=list[schemas.Agencia])
def listar_agencias(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_agencias(db, skip=skip, limit=limit)

@app.post("/agencias/", response_model=schemas.Agencia)
def criar_agencia(agencia: schemas.AgenciaCreate, db: Session = Depends(get_db)):
    return crud.create_agencia(db, agencia)

@app.get("/agencias/{id_agencia}", response_model=schemas.Agencia)
def obter_agencia(id_agencia: int, db: Session = Depends(get_db)):
    agencia = crud.get_agencia(db, id_agencia)
    if not agencia:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Agência não encontrada"
        )
    return agencia

# Rotas de Clientes
@app.get("/clientes/", response_model=list[schemas.Cliente])
def listar_clientes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_clientes(db, skip=skip, limit=limit)

@app.post("/clientes/", response_model=schemas.Cliente)
def criar_cliente(cliente: schemas.ClienteCreate, db: Session = Depends(get_db)):
    return crud.create_cliente(db, cliente)

# Rotas de Contas
@app.get("/contas/", response_model=list[schemas.Conta])
def listar_contas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_contas(db, skip=skip, limit=limit)

@app.post("/contas/", response_model=schemas.Conta)
def criar_conta(conta: schemas.ContaCreate, db: Session = Depends(get_db)):
    return crud.create_conta(db, conta)

# Rotas de Transações
@app.post("/transacoes/", response_model=schemas.Transacao)
def criar_transacao(transacao: schemas.TransacaoCreate, db: Session = Depends(get_db)):
    return crud.create_transacao(db, transacao)

@app.get("/transacoes/", response_model=list[schemas.Transacao])
def listar_transacoes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_transacoes(db, skip=skip, limit=limit)