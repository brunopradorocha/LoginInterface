# 🔐 Login Interface

Aplicação web desenvolvida em **Python + Streamlit** para criar um sistema simples de **autenticação de usuários**, com cadastro, login e armazenamento dos dados em um banco de dados PostgreSQL.

O projeto foi desenvolvido com foco em praticar integração entre uma aplicação Streamlit, banco de dados e sistema de autenticação.

## 🚀 Funcionalidades

- 🔑 Login de usuários
- 📝 Cadastro de novos usuários
- 🔒 Armazenamento seguro das senhas utilizando hash
- 🗄️ Integração com PostgreSQL
- 🚪 Logout
- 👤 Exibição do usuário autenticado
- 🍪 Gerenciamento de sessão utilizando cookies
- 🔄 Criação automática da tabela de usuários quando necessário

## 🛠️ Tecnologias utilizadas

- **Python 3.14**
- **Streamlit**
- **Streamlit Authenticator**
- **PostgreSQL 18**
- **Psycopg 3**
- **python-dotenv**

## 📂 Estrutura do projeto

```text
LoginInterface/
│
├── main.py
├── dependencies.py
├── .env
├── requirements.txt
└── README.md