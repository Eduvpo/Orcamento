import streamlit as st

def Read(cursor, conexao):
    st.write("Listando Receitas e Despesas:")
    tipo_registro = ['Receitas', 'Despesas']
    
    tipo = st.radio('Registro:', tipo_registro)

    if tipo == 'Receitas':

        comando = 'SELECT * FROM receitas'
        
        cursor.execute(comando)
        resultado = cursor.fetchall()

        total = 'SELECT sum(valor_r) FROM receitas'
        cursor.execute(total)
        resultado_t = cursor.fetchall()
        
        if resultado:
            st.table(resultado)
            st.write('Valor Total de Receitas')
            st.table(resultado_t)
        else:
            st.write("Nenhuma receita encontrada.")

    elif tipo == 'Despesas':

        comando = 'SELECT * FROM despesas'
        cursor.execute(comando)
        resultado = cursor.fetchall()

        total = 'SELECT sum(valor_d) FROM despesas'
        cursor.execute(total)
        resultado_t = cursor.fetchall()
    
        if resultado:
            st.table(resultado)
            st.write('Valor Total de Despesas')
            st.table(resultado_t)
    else:
        st.write("Nenhuma despesa encontrada.")
