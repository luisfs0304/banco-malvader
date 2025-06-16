from sqlalchemy import Column, Integer, String, Date, Text, ForeignKey, Enum, DECIMAL, Boolean
from sqlalchemy.orm import relationship
from .database import Base

class Usuario(Base):
    __tablename__ = "usuarios"
    id_usuario = Column(Integer, primary_key=True, index=True)
    login = Column(String(50), unique=True, nullable=False)
    senha = Column(String(100), nullable=False)
    nome = Column(String(100), nullable=False)
    otp_secret = Column(String(32), nullable=False)
    ativo = Column(Boolean, default=True)

class Agencia(Base):
    __tablename__ = "agencias"
    id_agencia = Column(Integer, primary_key=True, index=True)
    numero = Column(String(10), unique=True, nullable=False)
    nome = Column(String(100), nullable=False)
    endereco = Column(Text)
    contas = relationship("Conta", back_populates="agencia")

class Cliente(Base):
    __tablename__ = "clientes"
    id_cliente = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    cpf = Column(String(11), unique=True, nullable=False)
    data_nascimento = Column(Date)
    endereco = Column(Text)
    nivel_maldade = Column(Integer, default=0)
    contas = relationship("Conta", back_populates="cliente")

class Conta(Base):
    __tablename__ = "contas"
    id_conta = Column(Integer, primary_key=True, index=True)
    numero_conta = Column(String(20), unique=True, nullable=False)
    saldo = Column(DECIMAL(15, 2), default=0.00)
    tipo = Column(Enum("CORRENTE", "POUPANÇA", "BLACK_MALVADER", name="tipo_conta"), nullable=False)
    status = Column(Enum("ATIVA", "BLOQUEADA", "ENCERRADA", name="status_conta"), default="ATIVA")
    id_cliente = Column(Integer, ForeignKey("clientes.id_cliente"), nullable=False)
    id_agencia = Column(Integer, ForeignKey("agencias.id_agencia"), nullable=False)
    cliente = relationship("Cliente", back_populates="contas")
    agencia = relationship("Agencia", back_populates="contas")
    transacoes = relationship("Transacao", back_populates="conta")

class Transacao(Base):
    __tablename__ = "transacoes"
    id_transacao = Column(Integer, primary_key=True, index=True)
    tipo_transacao = Column(Enum("DEPÓSITO", "SAQUE", "TRANSFERÊNCIA", name="tipo_transacao"), nullable=False)
    valor = Column(DECIMAL(12, 2), nullable=False)
    data_transacao = Column(Date, nullable=False)
    numero_conta = Column(String(20), ForeignKey("contas.numero_conta"), nullable=False)
    conta = relationship("Conta", back_populates="transacoes")