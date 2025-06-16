from pydantic import BaseModel, Field
from typing import Optional
from datetime import date
from decimal import Decimal

# Schemas de Usuário
class UsuarioBase(BaseModel):
    login: str
    nome: str

class UsuarioCreate(UsuarioBase):
    senha: str

class Usuario(UsuarioBase):
    id_usuario: int
    ativo: bool

    class Config:
        orm_mode = True

# Schemas de Agência
class AgenciaBase(BaseModel):
    numero: str
    nome: str
    endereco: Optional[str] = None

class AgenciaCreate(AgenciaBase):
    pass

class Agencia(AgenciaBase):
    id_agencia: int

    class Config:
        orm_mode = True

# Schemas de Cliente
class ClienteBase(BaseModel):
    nome: str
    cpf: str
    data_nascimento: date
    endereco: str
    nivel_maldade: int = 0

class ClienteCreate(ClienteBase):
    pass

class Cliente(ClienteBase):
    id_cliente: int

    class Config:
        orm_mode = True

# Schemas de Conta
class ContaBase(BaseModel):
    numero_conta: str
    tipo: str = Field(..., description="Tipo de conta: CORRENTE, POUPANÇA ou BLACK_MALVADER")
    id_cliente: int
    id_agencia: int

class ContaCreate(ContaBase):
    pass

class Conta(ContaBase):
    id_conta: int
    saldo: Decimal
    status: str

    class Config:
        orm_mode = True

# Schemas de Token
class Token(BaseModel):
    access_token: str
    token_type: str
    otp: str

class TokenData(BaseModel):
    username: Optional[str] = None

# Schemas de Transação
class TransacaoBase(BaseModel):
    tipo_transacao: str = Field(..., description="Tipo de transação: DEPÓSITO, SAQUE ou TRANSFERÊNCIA")
    valor: Decimal = Field(..., gt=0)
    numero_conta: str

class TransacaoCreate(TransacaoBase):
    pass

class Transacao(TransacaoBase):
    id_transacao: int
    data_transacao: date

    class Config:
        orm_mode = True