-- CRIANDO O BANCO MALVADER 
CREATE DATABASE banco_malvader;
USE banco_malvader;

-- TABELA DE CLIENTES 
CREATE TABLE clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cpf CHAR(11) UNIQUE NOT NULL,
    data_nascimento DATE,
    endereco TEXT,
    nivel_maldade INT DEFAULT 0  -- tipo um medidor de encrenca
);

-- AGÊNCIAS DO MALVADER 
CREATE TABLE agencias (
    id_agencia INT AUTO_INCREMENT PRIMARY KEY,
    nome_agencia VARCHAR(100),
    cidade VARCHAR(100),
    codigo_agencia VARCHAR(10) UNIQUE
);

-- CONTAS 
CREATE TABLE contas (
    id_conta INT AUTO_INCREMENT PRIMARY KEY,
    numero_conta VARCHAR(20) UNIQUE NOT NULL,
    saldo DECIMAL(15, 2) DEFAULT 0.00,
    tipo ENUM('CORRENTE', 'POUPANÇA', 'BLACK MALVADER'),
    status ENUM('ATIVA', 'BLOQUEADA', 'ENCERRADA') DEFAULT 'ATIVA',
    id_cliente INT,
    id_agencia INT,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente),
    FOREIGN KEY (id_agencia) REFERENCES agencias(id_agencia)
);

-- TRANSACOES 
CREATE TABLE transacoes (
    id_transacao INT AUTO_INCREMENT PRIMARY KEY,
    tipo_transacao ENUM('DEPÓSITO', 'SAQUE', 'TRANSFERÊNCIA'),
    valor DECIMAL(12, 2) NOT NULL,
    data_transacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    id_conta_origem INT,
    id_conta_destino INT,
    FOREIGN KEY (id_conta_origem) REFERENCES contas(id_conta),
    FOREIGN KEY (id_conta_destino) REFERENCES contas(id_conta)
);

-- FUNCIONÁRIOS 
CREATE TABLE funcionarios (
    id_funcionario INT AUTO_INCREMENT PRIMARY KEY,
    nome_funcionario VARCHAR(100),
    cargo ENUM('GERENTE', 'ANALISTA', 'SUPERVISOR', 'SEGURANÇA'),
    nivel_acesso INT DEFAULT 1
);

-- USUÁRIOS DO SISTEMA 
CREATE TABLE usuarios (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    login VARCHAR(50) UNIQUE,
    senha VARCHAR(100),
    id_funcionario INT,
    FOREIGN KEY (id_funcionario) REFERENCES funcionarios(id_funcionario)
);





--  DADOS DE EXEMPLO (inserções de teste)
-- Criando uma agência de exemplo
INSERT INTO agencias (nome_agencia, cidade, codigo_agencia)
VALUES ('Matriz Malvader SP', 'São Paulo', 'MAL001');

-- Cadastrando o Carlos (aquele que vive no vermelho)
INSERT INTO clientes (nome, cpf, data_nascimento, endereco, nivel_maldade)
VALUES ('Carlos Trapaceiro', '12345678901', '1980-04-01', 'Rua do Golpe, 666', 7);

-- Criando uma conta pra ele
INSERT INTO contas (numero_conta, saldo, tipo, id_cliente, id_agencia)
VALUES ('00012345', 1200.00, '
