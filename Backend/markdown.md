# Banco Malvader

## 1. Objetivo do Trabalho

Desenvolver uma aplicação bancária chamada **Banco Malvader** com interface gráfica e persistência em banco de dados MySQL. O sistema deve gerenciar contas bancárias, funcionários e clientes, utilizando Programação Orientada a Objetos (POO) e recursos avançados de banco de dados, como gatilhos, procedures, views e auditoria.

---

## 2. Documento de Requisitos do Sistema (SRS)

### 2.1 Introdução

- **Objetivo:** Detalhar os requisitos funcionais, não funcionais e especificações do sistema Banco Malvader.
- **Escopo:** Gerenciamento de contas (Poupança, Corrente, Investimento), autenticação segura, relatórios financeiros, controle de funcionários e clientes, integração com MySQL.
- **Definições:**  
  - SRS: Software Requirements Specification  
  - POO: Programação Orientada a Objetos  
  - OTP: One-Time Password  
  - DAO: Data Access Object  
  - CPF: Cadastro de Pessoa Física  
  - CC: Conta Corrente  
  - CP: Conta Poupança  
  - CI: Conta Investimento

### 2.2 Referências

- [Documentação MySQL](https://dev.mysql.com/doc/)
- Livros: Date, Silberschatz, Deitel, Coronel, Fowler, Sommerville, Elmasri, Bates

---

## 3. Descrição Geral

### 3.1 Perspectiva do Produto

Sistema bancário completo, com interface gráfica e integração ao MySQL, para uso por funcionários e clientes.

### 3.2 Funções do Produto

- Autenticação multifator (senha + OTP)
- Gerenciamento de contas (abertura, encerramento, consulta, alteração)
- Operações financeiras (depósito, saque, transferência, extrato)
- Relatórios financeiros (exportação Excel/PDF)
- Auditoria de ações críticas
- Segurança (senhas fortes, limites, permissões)

### 3.3 Características dos Usuários

- **Funcionários:** Gerentes, atendentes, estagiários
- **Clientes:** Usuários finais
- **Desenvolvedores:** Alunos da UCB

### 3.4 Restrições

- Banco de dados obrigatoriamente em MySQL
- Regras críticas implementadas no banco
- Suporte a pelo menos 100 contas e 1.000 transações

### 3.5 Premissas e Dependências

- Ambiente MySQL configurado
- Uso de driver JDBC (ou equivalente)

---

## 4. Requisitos Específicos

### 4.1 Requisitos Funcionais

- **RF1:** Autenticação (senha + OTP, bloqueio após 3 tentativas)
- **RF2:** Menu Funcionário (abertura/encerramento de conta, consulta, alteração, cadastro de funcionários, relatórios)
- **RF3:** Menu Cliente (saldo, depósito, saque, transferência, extrato, consulta de limite, logout)

### 4.2 Requisitos Não Funcionais

- **RNF1:** Consultas em < 2 segundos
- **RNF2:** Suporte a 10.000 transações
- **RNF3:** Senhas criptografadas, auditoria, OTP
- **RNF4:** Interface intuitiva
- **RNF5:** Portabilidade (MySQL 8.x, front-end independente)

### 4.3 Requisitos de Interface

- Tela de login (senha + OTP)
- Menus com botões para funcionalidades
- Formulários com validação
- Relatórios e extratos tabulares, exportáveis

### 4.4 Requisitos de Banco de Dados

- Estrutura conforme seção 5
- Índices em campos de busca frequente
- Transações SQL para operações críticas
- Validações no banco

---

## 5. Estrutura do Banco de Dados

### 5.1 Tabelas Principais

- **usuario:** id_usuario, nome, cpf, data_nascimento, telefone, tipo_usuario, senha_hash, otp_ativo, otp_expiracao
- **funcionario:** id_funcionario, id_usuario, codigo_funcionario, cargo, id_supervisor
- **cliente:** id_cliente, id_usuario, score_credito
- **endereco, agencia, conta, conta_poupanca, conta_corrente, conta_investimento, transacao, auditoria, relatorio**

### 5.2 Gatilhos (Triggers)

- Atualização de saldo após transações
- Validação de senha forte
- Limite de depósito diário

### 5.3 Procedures

- **gerar_otp(id_usuario):** Gera OTP de 6 dígitos
- **calcular_score_credito(id_cliente):** Atualiza score do cliente

### 5.4 Visões (Views)

- **vw_resumo_contas:** Resumo de contas por cliente
- **vw_movimentacoes_recentes:** Movimentações dos últimos 90 dias

---

## 6. Estrutura do Projeto

- **dao:** Acesso ao banco de dados
- **model:** Classes das tabelas
- **view:** Interface gráfica (Swing, JavaFX, Web, etc.)
- **controller:** Lógica de negócios
- **util:** Conexão MySQL, utilitários

---

## 7. Critérios de Aceitação

- Todas as funcionalidades implementadas e testadas
- Banco de dados com tabelas, gatilhos, procedures e views funcionando
- Interface gráfica funcional e validada
- Documentação com diagrama ER e regras de negócio

---

## 8. Entrega

- **Código:** Organizado, comentado, com SQL detalhado
- **Documentação:** Diagrama ER, instruções de instalação, descrição do sistema
- **Apresentação:** Demonstração prática (5-10 minutos)

---

## 9. Critérios de Avaliação

- **Complexidade do Banco (30%)**
- **Integridade e Consistência (25%)**
- **Funcionalidade (25%)**
- **Interface e Usabilidade (20%)**

---

## 10. Bibliografia

- DATE, C. J. Introdução a Sistemas de Bancos de Dados. 8. ed. São Paulo: Pearson Addison Wesley, 2004.
- SILBERSCHATZ, Abraham; KORTH, Henry F.; SUDARSHAN, S. Sistemas de Banco de Dados. 6. ed. São Paulo: Pearson, 2013.
- DEITEL, Paul; DEITEL, Harvey. Java: Como Programar. 10. ed. São Paulo: Pearson, 2016.
- CORONEL, Carlos; MORRIS, Steven; ROB, Peter. Database Systems: Design, Implementation, & Management. 13th ed. Boston: Cengage Learning, 2019.
- FOWLER, Martin. UML Essencial: Um Breve Guia para a Linguagem Padrão de Modelagem de Objetos. 3. ed. Porto Alegre: Bookman, 2005.
- SOMMERVILLE, Ian. Engenharia de Software. 10. ed. São Paulo: Pearson, 2019.
- ELMASRI, Ramez; NAVATHE, Shamkant. Fundamentos de Sistemas de Banco de Dados. 7. ed. São Paulo: Pearson, 2016.
- BATES, Chris. Desenvolvimento de Websites com MySQL e PHP. 5. ed. São Paulo: Cengage Learning, 2017.

---

> **Observação:**  
> Para detalhes completos de tabelas, triggers, procedures e views, consulte o anexo SQL do projeto.

---

## 11. Atualizações e Progresso (16/06/2024)

### 11.1 Implementações Realizadas
- ✅ Estrutura básica do projeto FastAPI
- ✅ Conexão com banco de dados MySQL
- ✅ Autenticação básica com OTP
- ✅ CRUD de Agências
- ✅ CRUD de Clientes
- ✅ CRUD de Contas
- ✅ CRUD de Transações
- ✅ Validações básicas de negócio

### 11.2 Próximos Passos

#### 11.2.1 Autenticação e Segurança
- [ ] Implementar JWT token real (substituir "dummy_token")
- [ ] Adicionar bloqueio após 3 tentativas de login
- [ ] Implementar validação de senha forte
- [ ] Adicionar middleware de autenticação para rotas protegidas

#### 11.2.2 Funcionalidades de Conta
- [ ] Implementar tipos específicos de conta (Poupança, Corrente, Investimento)
- [ ] Adicionar limites de transação por tipo de conta
- [ ] Implementar consulta de saldo
- [ ] Desenvolver extrato detalhado
- [ ] Implementar transferência entre contas

#### 11.2.3 Funcionalidades de Cliente
- [ ] Implementar score de crédito
- [ ] Adicionar validação de CPF
- [ ] Desenvolver histórico de transações por cliente
- [ ] Implementar níveis de maldade com benefícios

#### 11.2.4 Funcionalidades de Funcionário
- [ ] Criar diferentes níveis de acesso (Gerente, Atendente, Estagiário)
- [ ] Implementar relatórios financeiros
- [ ] Adicionar aprovação de operações críticas
- [ ] Desenvolver dashboard administrativo

#### 11.2.5 Auditoria
- [ ] Implementar log de todas as operações críticas
- [ ] Criar histórico de alterações
- [ ] Desenvolver sistema de alertas
- [ ] Implementar relatórios de auditoria

#### 11.2.6 Relatórios
- [ ] Implementar exportação para Excel
- [ ] Adicionar exportação para PDF
- [ ] Desenvolver relatórios financeiros
- [ ] Criar dashboard com métricas importantes

### 11.3 Melhorias Técnicas Pendentes
- [ ] Otimizar consultas ao banco de dados
- [ ] Implementar cache para operações frequentes
- [ ] Adicionar testes unitários
- [ ] Implementar testes de integração
- [ ] Melhorar tratamento de erros
- [ ] Adicionar documentação detalhada da API
- [ ] Implementar rate limiting
- [ ] Adicionar monitoramento de performance

### 11.4 Prioridades Imediatas
1. Implementar JWT token real
2. Adicionar validações de negócio mais robustas
3. Implementar transferência entre contas
4. Desenvolver sistema de auditoria básico
5. Criar relatórios financeiros simples

---

> **Nota:** Este documento será atualizado conforme o progresso do desenvolvimento.
