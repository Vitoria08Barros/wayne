# 🦇 Wayne Industries – Sistema de Gerenciamento e Controle

## 📌 Descrição do Projeto

O sistema Wayne Industries é uma aplicação web full stack desenvolvida com o objetivo de simular um ambiente corporativo com autenticação de usuários, controle de acesso por níveis hierárquicos e gerenciamento de recursos internos.

A aplicação integra frontend e backend por meio de API REST, permitindo comunicação dinâmica entre as camadas do sistema.

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
- Redirecionamento de dashboard conforme perfil
- Cadastro e visualização de recursos
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
- Abrir MySQL
- Executar o arquivo:

database/wayne_db.sql


---

### 2. Backend (Flask)
No terminal, execute:

```bash id="p1q7lm"
python app.py

Servidor rodando em:

http://localhost:5000
Abrir o arquivo index.html no navegador
OU
Utilizar extensão Live Server no VS Code
🔗 Integração do Sistema

O frontend envia requisições HTTP para o backend utilizando Fetch API.

Fluxo do sistema:

Usuário realiza login
Frontend envia dados para API Flask
Backend valida no banco MySQL
Sistema retorna nível de acesso
Usuário é redirecionado para o painel correspondente
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
  "status": "success",
  "role": "administrador"
}
📁 Estrutura do Projeto
wayne-industries/
│
├── backend/
│   └── app.py
│
├── frontend/
│   ├── index.html
│   ├── admin.html
│   ├── gerente.html
│   └── funcionario.html
│
├── database/
│   └── wayne_db.sql
│
└── README.md
🎯 Objetivo Acadêmico

Este projeto tem como objetivo demonstrar a aplicação prática de conceitos de desenvolvimento full stack, incluindo:

Integração entre frontend e backend
Manipulação de banco de dados relacional
Implementação de autenticação de usuários
Organização de sistema web estruturado
Controle de acesso por níveis de permissão


🦇 Autor
Vitória Barros.

