# 🔐 Login Interface

Aplicação web desenvolvida em **Python + Streamlit** para criar um sistema simples de **autenticação de usuários**, com cadastro, login e armazenamento dos dados em um banco de dados PostgreSQL.

O projeto foi desenvolvido com foco em praticar a integração entre uma aplicação Streamlit, banco de dados PostgreSQL e sistema de autenticação de usuários.

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
- **Streamlit 1.64.0**
- **Streamlit Authenticator 0.4.2**
- **PostgreSQL 18**
- **Psycopg 3.3.6**
- **python-dotenv 1.2.3**

## 📂 Estrutura do projeto

```text
LoginInterface/
│
├── main.py
├── dependencies.py
├── .env
├── requirements.txt
└── README.md
```

### `main.py`

Responsável pela interface da aplicação e pelo fluxo de autenticação.

Principais responsabilidades:

- Exibir a tela de login
- Controlar o estado da sessão
- Realizar o cadastro de usuários
- Fazer o logout
- Exibir o conteúdo para usuários autenticados

### `dependencies.py`

Responsável pela comunicação com o PostgreSQL.

Contém funções para:

- Criar a tabela de usuários
- Consultar usuários
- Verificar se um nome de usuário já existe
- Inserir novos usuários no banco
- Gerenciar conexões com o PostgreSQL

## 🗄️ Banco de dados

O projeto utiliza uma tabela chamada `REGISTROS`:

```sql
CREATE TABLE REGISTROS (
    nome VARCHAR(255),
    usuario VARCHAR(255),
    senha VARCHAR(255)
);
```

As senhas dos usuários **não são armazenadas em texto puro**. Antes de serem salvas no banco de dados, elas são transformadas em hash através do `streamlit-authenticator`.

## 🔐 Configuração

As informações de conexão com o PostgreSQL são armazenadas em um arquivo `.env`.

Exemplo:

```env
DATABASE=auth_table
HOST=localhost
DB_USER=postgres
PASSWORD=sua_senha
PORT=5432
```

> ⚠️ O arquivo `.env` contém informações sensíveis e não deve ser enviado para o GitHub. Adicione o arquivo `.env` ao `.gitignore`.

## 📦 Instalação

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/LoginInterface.git
```

Entre na pasta do projeto:

```bash
cd LoginInterface
```

Instale as dependências:

```bash
python -m pip install -r requirements.txt
```

Configure o arquivo `.env` com os dados de acesso ao seu PostgreSQL.

## ▶️ Como executar

Após instalar as dependências e configurar o banco de dados, execute:

```bash
python -m streamlit run main.py
```

Após iniciar, o Streamlit disponibilizará a aplicação no navegador, normalmente através do endereço:

```text
http://localhost:8501
```

Acesse o endereço no navegador para utilizar o sistema.

## 📋 Requirements

As principais dependências utilizadas no projeto estão definidas no arquivo `requirements.txt`:

```text
streamlit==1.64.0
streamlit-authenticator==0.4.2
psycopg[binary]==3.3.6
python-dotenv==1.2.3
```

Para instalar todas as dependências:

```bash
python -m pip install -r requirements.txt
```

## 🎯 Objetivo do projeto

Este projeto foi desenvolvido como prática de **Python, Streamlit, PostgreSQL e autenticação de usuários**, explorando conceitos como:

- Integração entre Python e banco de dados
- CRUD básico
- Hash de senhas
- Gerenciamento de sessões
- Variáveis de ambiente
- Conexão com PostgreSQL
- Estruturação de aplicações Streamlit
- Separação entre interface e acesso ao banco de dados

## 📚 Aprendizados

Durante o desenvolvimento foram trabalhados conceitos importantes como:

- Utilização de `st.session_state`
- Criação de formulários com `st.form`
- Autenticação com `streamlit-authenticator`
- Hash de senhas
- Consultas parametrizadas no PostgreSQL
- Gerenciamento de conexões utilizando `contextmanager`
- Separação da lógica da aplicação e acesso ao banco de dados
- Configuração de ambiente utilizando `.env`
- Gerenciamento de dependências através do `requirements.txt`

---

## 👨‍💻 Projeto desenvolvido para estudos

Projeto criado com o objetivo de colocar em prática conceitos de desenvolvimento web utilizando **Python, Streamlit e PostgreSQL**.