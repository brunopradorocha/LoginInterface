import streamlit as st
import streamlit_authenticator as stauth
from streamlit_authenticator.utilities import Hasher
from time import sleep

##################################################
# Funções
##################################################

def main():
    authenticator = stauth.Authenticate(
        {'usernames': {'teste': {'name': 'testando', 'password':'blabla'}}},
        'random_coockie_name',
        'random_signature_key',
        cookie_expiry_days = 30, # Expira em 30 dias
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
        authenticator.lougot('Logout', main) # Inclui um botão de logout
        # Login realizado com sucesso
        st.title('Área do dashboard')
        st.write(f'Bem-vindo! {st.session_state.get('name')}')
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
    st.write(hashed_password)
    if st.session_state.passwd != st.session_state.confirm_passwd:
        st.warning('As senhas não conferem!')
        sleep(5)
    elif 'consulta_nome()':
        st.warning('Nome de usuário já existe')
        sleep(5)
    else:
        #'add_registro()'
        st.success("Registro efetuado!")

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