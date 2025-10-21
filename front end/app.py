import streamlit as st
import requests as rq
API_URL =  "http://127.0.0.1:8000"
st.set_page_config(page_title="Gerenciador de estoque", page_icon="📉")
menu = st.sidebar.radio("📋 Menu", [
    "📦 Catálogo",
    "➕ Adicionar Produto",
    "✏️ Atualizar Produto",
    "❌ Deletar Produto"
])
if menu == "📦 Catálogo":
    st.subheader("Todos os produtos")
    response = rq.get(f"{API_URL}/produtos")
    if response.status_code == 200:
        produtos = response.json().get("produtos", [])
        if produtos:
            for produto in produtos:
                st.write(f"{produto['nome']} // {produto['categoria']} // {produto['preco']}  // {produto['quantidade']}")
        else:
            st.info("Nenhum produto encontrado🔈")
    else:
        st.error("Erro ao conectar API")

if menu == "➕ Adicionar Produto":
    st.subheader("Inserir Produto ➕")
    nome = st.text_input("Nome Produto")
    categoria = st.text_input("Categoria Produto")
    preco = st.number_input("Valor do Produto")
    quantidade = st.number_input("Digite a quantidade do Produto")

    if st.button("Finalizar Cadastro Produtos"):
        params = {"nome": nome, "categoria": categoria, "preco": preco, "quantidade": quantidade}
        response = rq.post(f"{API_URL}/produtos", params=params)
        print(response.status_code)
        if response.status_code == 200:
            st.success(" Produto adicionado com sucesso! ✔")
        else:

            st.error("Error!")

elif menu == "✏️ Atualizar Produto":
    st.subheader("Atualizar Produto ✏️")
    id_produto = st.number_input("ID do Produto a atualizar", step=1, format="%d")
    
    novo_nome = st.text_input("Novo Nome")
    nova_categoria = st.text_input("Nova Categoria")
    novo_preco = st.number_input("Novo Preço", format="%.2f")
    nova_quantidade = st.number_input("Nova Quantidade", step=1, format="%d")
    
    if st.button("Atualizar"):
        params = {}
        if novo_nome: params["nome"] = novo_nome
        if nova_categoria: params["categoria"] = nova_categoria
        if novo_preco: params["preco"] = novo_preco
        if nova_quantidade: params["quantidade"] = nova_quantidade

        if params:
            response = rq.post(f"{API_URL}/produtos", params=params)
            if response.status_code == 200:
                st.success("Produto atualizado com sucesso!")
            else:
                st.error("Erro ao atualizar produto.")
        else:
            st.warning("Preencha ao menos um campo para atualizar.")


elif menu == "❌ Deletar Produto":
    st.subheader("Deletar Produto ✖")
    id_produto  = st.number_input("ID do produto a deletar", step=1, format="%d")
    
    if st.button("Deletar"):
        response = rq.delete(f"{API_URL}/produtos/{id_produto }")
        if response.status_code == 200:
            st.success("Produto deletado com sucesso! ✔")
        else:
            st.error(f"Erro {response.status_code}: {response.text}")