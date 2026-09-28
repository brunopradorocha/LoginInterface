import streamlit as st
import streamlit_authenticator as stauth

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


if __name__ == '__main__': 
    main()