# 🦇 Wayne Industries – Sistema de Gerenciamento e Controle

## 📌 Descrição do Projeto

O sistema Wayne Industries é uma aplicação web full stack desenvolvida com o objetivo de simular um ambiente corporativo seguro, com autenticação de usuários, controle de acesso baseado em níveis hierárquicos e gerenciamento de recursos internos.

A aplicação segue o modelo cliente-servidor, integrando frontend e backend por meio de uma API REST, garantindo comunicação eficiente, segura e dinâmica entre as camadas do sistema.

---

## ⚙️ Tecnologias Utilizadas

### Backend
- Python
- Flask
- Flask-CORS

### Banco de Dados
- MySQL

### Frontend
- HTML5
- CSS3
- JavaScript (Fetch API)

---

## 🧠 Funcionalidades

- Sistema de login com autenticação de usuários
- Controle de acesso por níveis:
  - Administrador
  - Gerente
  - Funcionário
- Restrição de acesso a funcionalidades conforme o perfil do usuário
- Cadastro, edição, exclusão e visualização de recursos (CRUD completo)
- Dashboard com visualização de dados
- Integração entre frontend e backend
- Comunicação via API REST (JSON)

---

## 🗄️ Banco de Dados

O sistema utiliza o MySQL com duas tabelas principais:

### Tabela: usuarios
- id
- username
- password
- nome
- role

### Tabela: recursos
- id
- nome
- tipo
- status
- quantidade

📁 O script completo do banco está disponível no arquivo:


database/wayne_db.sql


---

## 🔐 Acesso ao Sistema (Teste)

Credenciais para avaliação:

### 🛡️ Administrador
- Usuário: admin  
- Senha: 1234  

### 📊 Gerente
- Usuário: gerente  
- Senha: 1234  

### 👷 Funcionário
- Usuário: funcionario  
- Senha: 1234  

---

## 🚀 Como Executar o Projeto

### 1. Banco de Dados
- Abrir o MySQL
- Executar o arquivo:


database/wayne_db.sql


---

### 2. Backend (Flask)

No terminal, execute:

```bash
python app.py

Servidor rodando em:

http://localhost:5000
3. Frontend

Abrir o arquivo index.html utilizando um servidor local (recomendado: Live Server no VS Code).

🔗 Integração do Sistema

O frontend envia requisições HTTP para o backend utilizando Fetch API.

Fluxo do sistema:
Usuário realiza login
Frontend envia dados para API Flask
Backend valida no banco MySQL
Sistema retorna os dados do usuário
O frontend controla o acesso conforme o nível (role)
Usuário acessa funcionalidades permitidas
🧪 Endpoint da API
POST /login

Descrição: Autentica usuário no sistema

Body (JSON):
{
  "username": "admin",
  "password": "1234"
}
Resposta de sucesso:
{
  "id": 1,
  "username": "admin",
  "nome": "Bruce Wayne",
  "role": "administrador"
}
🔄 Operações CRUD

O sistema permite operações completas de CRUD (Create, Read, Update, Delete) sobre os recursos:

Criar novos recursos
Listar recursos existentes
Atualizar informações
Deletar registros
📁 Estrutura do Projeto
wayne-industries/
│
├── backend/
│   └── app.py
│
├── frontend/
│   └── index.html
│
├── database/
│   └── wayne_db.sql
│
└── README.md
🔐 Segurança

Para fins acadêmicos, as senhas estão armazenadas em formato simples.

Em um ambiente real, seria utilizada criptografia (ex: bcrypt) para proteção dos dados dos usuários.

🎯 Objetivo Acadêmico

Este projeto tem como objetivo demonstrar a aplicação prática de conceitos de desenvolvimento full stack, incluindo:

Integração entre frontend e backend
Manipulação de banco de dados relacional
Implementação de autenticação de usuários
Organização de sistema web estruturado
Controle de acesso por níveis de permissão
🌐 Observações
O sistema foi desenvolvido para fins acadêmicos
Algumas funcionalidades utilizam dados simulados no frontend
O backend implementa controle de acesso real baseado em permissões


🦇 Autor
Vitória Barros
