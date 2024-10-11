import streamlit as st
import mysql.connector

from orcamento.create import Create
from orcamento.read import Read
from orcamento.update import Update
from orcamento.delete import Delete

conexao = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='root',
    database='orcamento',
    port='8889'
)

cursor = conexao.cursor()

def main():
    st.title("Orçamento Mensal")
    
    menu = ['Inserir', 'Visualizar', 'Atualizar', 'Excluir', 'Sair']
    choice = st.sidebar.selectbox("Escolha uma opção", menu)
    
    if choice == 'Inserir':
        st.subheader("Inserir novo registro")
        Create(cursor, conexao)
        
    elif choice == 'Visualizar':
        st.subheader("Visualizar registros")
        Read(cursor, conexao)
        
    elif choice == 'Atualizar':
        st.subheader("Atualizar registro")
        opcao = st.radio("Deseja ver a lista antes de atualizar?", ('Sim', 'Não'))
        
        if opcao == 'Sim':
            Read(cursor, conexao)
            Update(cursor, conexao)
        else:
            Update(cursor, conexao)
    
    elif choice == 'Excluir':
        st.subheader("Excluir registro")
        Delete(cursor, conexao)
        
    elif choice == 'Sair':
        st.write("Programa encerrado.")
        st.stop()
    
if __name__ == '__main__':
    main()
