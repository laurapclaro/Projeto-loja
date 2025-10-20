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
