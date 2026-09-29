import streamlit as st
import streamlit_authenticator as stauth
from streamlit_authenticator.utilities import Hasher
from time import sleep
from dependencies import consulta_geral,consulta_username,add_registro,cria_tabela

##################################################
# Funções
##################################################

def main():

    try:
        consulta_geral()
    except:
        cria_tabela()

    # Retorna uma lista com 3 colunas: nome, username, senha
    db_query = consulta_geral()

    # Criação do cabeçalho usado na autenticação
    registros = { 'usernames': { } }
    for data in db_query:
        registros['usernames'][data[1]] = {'name': data[0], 'password': data[2]}


    authenticator = stauth.Authenticate(
        registros,
        'random_coockie_name',
        'random_signature_key',
        cookie_expiry_days = 30, # autenticação expira em 30 dias
    )

    if 'registrar' not in st.session_state:
        st.session_state['registrar'] = False
    
    if st.session_state['registrar'] == False:
        login_form(authenticator)
    else:
        usuario_form()
        
def login_form(authenticator):
    authenticator.login(location='main')
    if st.session_state.get('authentication_status'):
        authenticator.logout(location='main')  
        # Login realizado com sucesso
        st.title('Área do dashboard')
        st.write(f"Bem-vindo! {st.session_state.get('name')}")
    elif st.session_state.get('authentication_status') == False:
        # Erro ao validar as credenciais informadas
        st.error('Usuário/Senha inválidos!')
    elif st.session_state.get('authentication_status') == None:
        # Status inicial da tela de login
        st.warning('Por favor informe um usuário e senha!')
    registrar = st.button("Registrar")
    if registrar:
        st.session_state['registrar'] = True
        st.rerun()
def confirm_msg():
    hashed_password = Hasher().hash(st.session_state["passwd"])
    if st.session_state.passwd != st.session_state.confirm_passwd:
        st.warning('As senhas não conferem!')
        sleep(3)
    elif consulta_username(st.session_state['user']):
        st.warning('Nome de usuário já existe')
        sleep(3)
    else:
        add_registro(st.session_state["nome"] , st.session_state["user"] , hashed_password)
        st.success("Registro efetuado!")
        sleep(3)

def usuario_form():
    with st.form(key="formulario", clear_on_submit=True):
        nome = st.text_input("Nome", key="nome")
        username = st.text_input("Usuario", key="user")
        password = st.text_input("Senha", key="passwd", type="password")
        confirm_password = st.text_input("Confirme a senha", key="confirm_passwd", type="password")
        submit = st.form_submit_button(
            "Salvar", on_click=confirm_msg
        )
    clicou_em_fazer_login = st.button("Voltar para a tela de login")
    if clicou_em_fazer_login:
        st.session_state['registrar'] = False
        st.rerun()

##################################################
# Main
##################################################

if __name__ == '__main__': 
    main()