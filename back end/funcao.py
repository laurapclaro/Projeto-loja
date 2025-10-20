from conexao import conectar

def criar_tabela():
    conexao, cursor = conectar()
    if conexao:
        try: 
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS produtos (
               id SERIAL,
                nome VARCHAR(100) NOT NULL,
                categoria VARCHAR(50),
                preco DECIMAL(10,2),
                quantidade INT )


""")
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao criar tabela {erro}")
        finally:
            cursor.close()
            conexao.close()


criar_tabela()


#-----------

def adicionar_produto(nome, categoria, preco, quantidade):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "INSERT INTO produto (nome, categoria, preco, quantidade) VALUES (%s, %s, %s, %s)",
                (nome, categoria, preco, quantidade)
            )
            conexao.comit()
        except Exception as erro:
            print(F"Erro ao inserir {erro}")
        finally:
            cursor.close()
            conexao.close()

#-----------

def listar_total():
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "SELECT * FROM produto ORDER BY id"
            )
            return cursor.fetchall()
        except Exception as erro:
            print(f"Erro ao listar {erro}")
            return []
        finally:
            cursor.close()
            conexao.close()

produtos = listar_total()
print(produtos)

#------------

def atualizar_preco_quantidade(preco, quantidade):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "UPDAT produto SET preco = %s WHERE id = %s",
                "UPDATE produto SET quantidade = %s WHERE id = %s",
                (quantidade, preco)
            )
            conexao.commit()
        except Exception as erro:
            print(f"Erro as atualizar a nota: {erro}")
        finally:
            cursor.close()
            conexao.close()

#------------

def deletar_movie(id_produto):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "DELETE FROM produto WHERE id = %s, (id_produto,)"
            )
            conexao.comit()
        except Exception as erro:
            print(f"Erro ao deletar filme: {erro}")
        finally:
            cursor.close()
            conexao.close()

#-------------

def pesquisar_produto(nome_parcial):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "SELECT * FROM produto WHERE nome ILIKE %s ORDER BY id",
                (f"%{nome_parcial}%", )
            )
            resultados = cursor.fetchall()
            return resultados
        except Exception as erro:
            print(f"Erro ao pesquisar produtp: {erro}")
            return []
        finally:
            cursor.close()
            conexao.close()