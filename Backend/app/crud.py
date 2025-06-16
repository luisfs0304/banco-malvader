from sqlalchemy.orm import Session
from . import models, schemas
import pyotp
from passlib.context import CryptContext
from datetime import date
from fastapi import HTTPException, status
from decimal import Decimal

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Funções de Autenticação
def get_user_by_login(db: Session, login: str):
    return db.query(models.Usuario).filter(models.Usuario.login == login).first()

def authenticate_user(db: Session, login: str, password: str):
    user = get_user_by_login(db, login)
    if not user:
        return False
    if not verify_password(password, user.senha):
        return False
    return user

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

# Funções de Cliente
def get_clientes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Cliente).offset(skip).limit(limit).all()

def create_cliente(db: Session, cliente: schemas.ClienteCreate):
    db_cliente = models.Cliente(**cliente.dict())
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente

# Funções de Agência
def get_agencias(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Agencia).offset(skip).limit(limit).all()

def get_agencia(db: Session, id_agencia: int):
    return db.query(models.Agencia).filter(models.Agencia.id_agencia == id_agencia).first()

def create_agencia(db: Session, agencia: schemas.AgenciaCreate):
    db_agencia = models.Agencia(**agencia.dict())
    db.add(db_agencia)
    db.commit()
    db.refresh(db_agencia)
    return db_agencia

# Funções de Conta
def get_contas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Conta).offset(skip).limit(limit).all()

def create_conta(db: Session, conta: schemas.ContaCreate):
    # Validar se o cliente existe
    cliente = db.query(models.Cliente).filter(models.Cliente.id_cliente == conta.id_cliente).first()
    if not cliente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cliente não encontrado"
        )
    
    # Validar se a agência existe
    agencia = get_agencia(db, conta.id_agencia)
    if not agencia:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Agência não encontrada"
        )
    
    # Validar tipo de conta
    if conta.tipo not in ["CORRENTE", "POUPANÇA", "BLACK_MALVADER"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Tipo de conta inválido"
        )
    
    db_conta = models.Conta(**conta.dict())
    db.add(db_conta)
    db.commit()
    db.refresh(db_conta)
    return db_conta

def get_conta_by_numero(db: Session, numero_conta: str):
    conta = db.query(models.Conta).filter(models.Conta.numero_conta == numero_conta).first()
    if not conta:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Conta não encontrada"
        )
    return conta

# Funções de Transação
def get_transacoes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Transacao).offset(skip).limit(limit).all()

def create_transacao(db: Session, transacao: schemas.TransacaoCreate):
    # Validar se a conta existe
    conta = get_conta_by_numero(db, transacao.numero_conta)
    
    # Validar tipo de transação
    if transacao.tipo_transacao not in ["DEPÓSITO", "SAQUE", "TRANSFERÊNCIA"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Tipo de transação inválido"
        )
    
    # Validar valor
    if transacao.valor <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Valor deve ser maior que zero"
        )
    
    # Validar saldo para saque
    if transacao.tipo_transacao == "SAQUE" and conta.saldo < transacao.valor:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Saldo insuficiente"
        )
    
    db_transacao = models.Transacao(
        **transacao.dict(),
        data_transacao=date.today()
    )
    db.add(db_transacao)
    
    # Atualizar saldo da conta
    if transacao.tipo_transacao == "DEPÓSITO":
        conta.saldo += Decimal(str(transacao.valor))
    elif transacao.tipo_transacao == "SAQUE":
        conta.saldo -= Decimal(str(transacao.valor))
    
    db.commit()
    db.refresh(db_transacao)
    return db_transacao

    