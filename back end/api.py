from fastapi import FastAPI
import funcao

app = FastAPI(title="Gerenciador de estoque")
#GET
#POST
#PUT
#DELETE

@app.get("/")
def home():
    return {"mensagem": "Bem - vindo ao estoque!"}
#________________

@app.get("/produtos")
def catalogo():
    produtos = funcao.listar_produtos()
    lista = []
    for produto in produtos:
        lista.append({
            "id": produto[0],
            "nome": produto[1],
            "categoria": produto[2],
            "preco": produto[3],
            "quantidade": produto[4]
        })
    return {"produtos": lista}
#____________________

@app.post("/produtos")
def adicionar_produto(nome: str, categoria: str, preco: float, quantidade: int):
    funcao.adicionar_produto(nome, categoria, preco, quantidade)
    return {"mensagem": "Produto adicionado com sucesso!"}
#__________

@app.put("/produtos/{id_produto}")
def atualizar_estoque(id_produto: int,
                    preco: float,
                    quantidade: int
    ):
    produtos = funcao.buscar_produto(id_produto)
    if produtos:
        funcao.atualizar_preco_quantidade(id_produto)
        return{"mensagem": "Produto atualizado"}
    return {"error": "Produto não encontrado"}
#________________________

@app.delete("/produtos/{id_produto}")
def deletar_produto_route(id_produto: int):
    produto = funcao.buscar_produto(id_produto)
    if produto:
        funcao.deletar_produto(id_produto)
        return {"mensagem": f"Produto {id_produto} deletado com sucesso!"}
   




