import streamlit as st

def Delete(cursor, conexao):
    opcao_1 = st.radio('Qual a opção desejada?', ('Receitas','Despesas'))

    if opcao_1 == 'Receitas':

        ver_lista = st.radio('Você deseja ver a lista de receitas antes de apagar?', ('Sim', 'Não'))

        if ver_lista == 'Sim':
            comando = 'SELECT * FROM receitas'
            cursor.execute(comando)
            resultado = cursor.fetchall()
            
            if resultado:
                st.write("Lista de Receitas:")
                st.table(resultado)
            else:
                st.write("Nenhuma receita encontrada.")
        
        opcao = st.selectbox("Escolha um critério para exclusão:", ["Selecione", "ID", "Nome"])
        
        if opcao == "ID":
            id_rec = st.text_input('Informe o ID que deseja apagar:')
            if st.button('Deletar por ID'):
                if id_rec:
                    comando = 'DELETE FROM receitas WHERE id_rec = %s;'
                    cursor.execute(comando, (id_rec,))
                    conexao.commit()
                    st.success(f'Receita com ID {id_rec} deletado com sucesso.')
                else:
                    st.error('Por favor, insira um ID válido.')
        
        elif opcao == "Nome":
            nome_r = st.text_input('Informe o nome que deseja apagar:')
            if st.button('Deletar por Nome'):
                if nome_r:
                    comando = 'DELETE FROM receitas WHERE nome_r = %s;'
                    cursor.execute(comando, (nome_r,))
                    conexao.commit()
                    st.success(f'Receita com nome {nome_r} deletado com sucesso.')
                else:
                    st.error('Por favor, insira um nome válido.')
        else:
            st.warning('Por favor, selecione uma opção válida para exclusão.')
    
    elif opcao_1 == 'Despesas':

        ver_lista = st.radio('Você deseja ver a lista de despesas antes de apagar?', ('Sim', 'Não'))

        if ver_lista == 'Sim':
            comando = 'SELECT * FROM despesas'
            cursor.execute(comando)
            resultado = cursor.fetchall()
            
            if resultado:
                st.write("Lista de Despesas:")
                st.table(resultado)
            else:
                st.write("Nenhuma despesa encontrada.")
        
        opcao = st.selectbox("Escolha um critério para exclusão:", ["Selecione", "ID", "Nome"])
        
        if opcao == "ID":
            id_des = st.text_input('Informe o ID que deseja apagar:')
            if st.button('Deletar por ID'):
                if id_des:
                    comando = 'DELETE FROM despesas WHERE id_des = %s;'
                    cursor.execute(comando, (id_des,))
                    conexao.commit()
                    st.success(f'Receita com ID {id_des} deletado com sucesso.')
                else:
                    st.error('Por favor, insira um ID válido.')
        
        elif opcao == "Nome":
            nome_d = st.text_input('Informe o nome que deseja apagar:')
            if st.button('Deletar por Nome'):
                if nome_d:
                    comando = 'DELETE FROM despesas WHERE nome_d = %s;'
                    cursor.execute(comando, (nome_d,))
                    conexao.commit()
                    st.success(f'Despesa com nome {nome_d} deletado com sucesso.')
                else:
                    st.error('Por favor, insira um nome válido.')
        else:
            st.warning('Por favor, selecione uma opção válida para exclusão.')

