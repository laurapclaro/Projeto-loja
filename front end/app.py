import streamlit as st
import requests as rq
API_URL =  "http://127.0.0.1:8000"
st.set_page_config(page_title="Gerenciador de estoque", page_icon="📉")
menu = st.sidebar.radio("Navegação", ["Catálogo", "Adicionar Produto", "Atualizar produto", "Deletar Produtos"  ])

if menu == "Catálogo":
    st.subheader("Todos os produtos")
    response = rq.get(f"{API_URL}/produtos")
    if response.status_code == 200:
        produtos = response.json().get("produtos", [])
        if produtos:
            for produto in produtos:
                st.write(F" **{produto['nome']}** // {produto['categoria']} // {produto['preco']} // {produto['quantidade']}")
        else:
            st.info("Nenhum produto encontrado🔈")

    else:
        st.error("Erro ao conectar API")