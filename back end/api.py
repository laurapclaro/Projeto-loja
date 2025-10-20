from fastapi import FastAPI
import funcao


app = FastAPI(tittle="Gerenciador de estoque")
#GET
#POST
#PUT
#DELETE

@app.get("/")
def home():
    return {"mensagem": "Bem - vindo ao estoque!"}

@app.get("/produtos")
def catalogo():
    produtos = funcao.listar_total
    lista = []
    for produto in produtos:
        lista.append( { "id": produto[0], 
                    "nome": produto[1], 
                    "categoria": produto[2],
                    "preco": produto[3],
                     "quantidade": produto[4] 
                     })
    return{"filmes": lista}



@app.post("/produtos")
def adicionar_produto(nome: str, categoria: str, preco: float, quantidade: str):
    funcao.criar_produto(nome, categoria, preco, quantidade)
    return("mensagem: produto adicionado com sucesso!")

@app.put("/produtos/{id_produto}")
def atualizar_estoque(id_produto: int):
    produtos = funcao.buscar_produto(id_produto)
    if produtos:
        funcao.atualizar_produto(id_produto)
        return{"mensagem": "Produto atualizado"}
    return {"error": "Produto não encontrado"}

@app.delete("/produto/{id_produto}")
def deletar_produto(id_produto: int):
    produto = funcao.buscar_produto(id_produto)
    if produto:
        funcao.deletar_produto(id_produto)
    return {"mensagem": f"Produto {id_produto} deletado com sucesso!"}
