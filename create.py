import streamlit as st

def Create(cursor, conexao):
    st.write("Cadastro de nova receita")
    tipo_registro = ['Receita', 'Despesa']
    
    tipo = st.radio('Registro:', tipo_registro)

    if tipo == 'Receita':
    
        receita = st.text_input('Informe o nome da receita:')
        valor = st.number_input('Informe o valor da receita:', min_value=0.0, step=0.01, format="%.2f")
    
    elif tipo == 'Despesa':

        despesa = st.text_input('Informe o nome da despesa:')
        valor_d = st.number_input('Informe o valor da despesa:', min_value=0.0, step=0.01, format="%.2f")
    
    if st.button('Inserir Registro'):
        match tipo:
            case 'Receita': 

                comando = 'INSERT INTO receitas (nome_r, valor_r) VALUES (%s, %s)'
                cursor.execute(comando, (receita, valor))
                conexao.commit()
                st.success('Receita cadastrada com sucesso.')

            case 'Despesa':
                comando = 'INSERT INTO despesas (nome_d, valor_d) VALUES (%s, %s)'
                cursor.execute(comando, (despesa, valor_d))
                conexao.commit()
                st.success('Despesa cadastrada com sucesso.')

            case _: 
                st.error("Por favor, insira um nome válido e um preço maior que zero.")
