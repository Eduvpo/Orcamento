import streamlit as st

def Update(cursor, conexao):
    st.write("Atualizar o valor de um Registro")

    tipo_registro = ['Receita', 'Despesa']
    
    tipo2 = st.radio('Registro:', tipo_registro)

    if tipo2 == 'Receita':

        receita = st.text_input('Digite o nome da receita:')
        valor_r = st.number_input('Informe o novo valor da receita:', min_value=0, step=1)

    elif tipo2 == 'Despesa':

        despesa = st.text_input('Digite o nome da despesa:')
        valor_d = st.number_input('Informe o novo valor da despesa:', min_value=0, step=1)
    
    if st.button('Atualizar Registro'):
        match tipo2:
            case 'Receita':
                comando = f'UPDATE receitas SET valor_r = {valor_r} WHERE nome_r = "{receita}"'
                cursor.execute(comando)
                conexao.commit()
                st.success(f'O valor da receita {receita} foi atualizado para {valor_r}.')
            case 'Despesa':
                comando = f'UPDATE despesas SET valor_d = {valor_d} WHERE nome_d = "{despesa}"'
                cursor.execute(comando)
                conexao.commit()
                st.success(f'O valor da despesa {despesa} foi atualizado para {valor_d}.')
            case _:
                st.error("Por favor, insira um nome de despesa válida e um valor maior que zero.")
