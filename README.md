# 🏦 Banco Malvader

Sistema bancário desenvolvido com FastAPI e MySQL, oferecendo uma experiência única de banco digital com um toque de maldade.

## 📋 Descrição

O Banco Malvader é um sistema bancário completo que gerencia contas, clientes, agências e transações. O sistema inclui autenticação segura com OTP (One-Time Password), diferentes tipos de contas e um sistema de níveis de "maldade" para os clientes.

## 📁 Estrutura do Projeto

```
banco-malvader/
├── Backend/           # API REST com FastAPI
│   ├── app/          # Código fonte da aplicação
│   ├── venv/         # Ambiente virtual Python
│   └── requirements.txt
└── Frontend/         # Interface do usuário (em desenvolvimento)
```

## 🚀 Tecnologias Utilizadas

### Backend
- Python 3.13+
- FastAPI
- SQLAlchemy
- MySQL
- PyOTP (Autenticação OTP)
- Pydantic
- Uvicorn

### Frontend (Em desenvolvimento)
- React.js
- TypeScript
- Material-UI
- Axios

## ⚙️ Requisitos

### Backend
- Python 3.13 ou superior
- MySQL 8.0 ou superior
- pip (gerenciador de pacotes Python)

### Frontend (Em desenvolvimento)
- Node.js 18+
- npm ou yarn

## 🛠️ Instalação

### Backend

1. Clone o repositório:
```bash
git clone https://github.com/ArthurClaro/banco-malvader.git
cd banco-malvader/Backend
```

2. Crie e ative o ambiente virtual:
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure o banco de dados:
- Crie um banco de dados MySQL
- Configure as variáveis de ambiente no arquivo `.env`:
```env
DATABASE_URL=mysql+pymysql://usuario:senha@localhost:3306/banco_malvader
```

5. Inicie o servidor:
```bash
uvicorn app.main:app --reload
```

### Frontend (Em desenvolvimento)
```bash
cd ../Frontend
npm install
npm start
```

## 📚 Documentação da API

A documentação completa da API está disponível em:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## 🔑 Rotas Principais

### Autenticação
- `POST /primeiro-usuario/` - Criar primeiro usuário (admin)
- `POST /token` - Login com OTP

### Agências
- `GET /agencias/` - Listar agências
- `POST /agencias/` - Criar agência
- `GET /agencias/{id_agencia}` - Obter agência específica

### Clientes
- `GET /clientes/` - Listar clientes
- `POST /clientes/` - Criar cliente

### Contas
- `GET /contas/` - Listar contas
- `POST /contas/` - Criar conta

### Transações
- `GET /transacoes/` - Listar transações
- `POST /transacoes/` - Criar transação

## 🎯 Funcionalidades

### Backend
- ✅ Autenticação com OTP
- ✅ Gerenciamento de agências
- ✅ Gerenciamento de clientes
- ✅ Diferentes tipos de contas
- ✅ Sistema de transações
- ✅ Níveis de "maldade" para clientes

### Frontend (Em desenvolvimento)
- [ ] Interface responsiva
- [ ] Dashboard administrativo
- [ ] Área do cliente
- [ ] Relatórios gráficos
- [ ] Gestão de contas

## 🔜 Próximas Implementações

### Backend
- [ ] JWT Token real
- [ ] Transferência entre contas
- [ ] Sistema de auditoria
- [ ] Relatórios financeiros
- [ ] Dashboard administrativo

### Frontend
- [ ] Implementação da interface
- [ ] Integração com a API
- [ ] Sistema de autenticação
- [ ] Dashboard interativo
- [ ] Relatórios visuais

## 🤝 Contribuindo

1. Faça um Fork do projeto
2. Crie uma Branch para sua Feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a Branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👥 Autores

- Arthur Claro - [@ArthurClaro](https://github.com/ArthurClaro)

## 🙏 Agradecimentos

- FastAPI
- SQLAlchemy
- Comunidade Python
- Todos os contribuidores

---

⭐️ From [ArthurClaro](https://github.com/ArthurClaro)
