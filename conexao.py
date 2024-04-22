import mysql.connector
from credenciais import HOST, USER, PASSWORD, DATABASE


def conectar():
    # Iniciar conexão
    conexao = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )
    return conexao

def obter_lista():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM lista')
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultado

def Adicionar(nome, quantidade, preco, local):
    conexao = conectar()
    cursor = conexao.cursor()
    comando = f'INSERT INTO lista (name, quantidade, preco, local) VALUES ("{nome}", {quantidade}, {preco}, "{local}")'
    cursor.execute(comando)
    conexao.commit()
    cursor.close()
    conexao.close()

def Editar(nome, quantidade, preco, local):
    conexao = conectar()
    cursor = conexao.cursor()
    comando = f'UPDATE lista SET quantidade = {quantidade}, preco = {preco}, local = "{local}" WHERE name = "{nome}"'
    cursor.execute(comando)
    conexao.commit()
    cursor.close()
    conexao.close()

def Apagar(nome):
    conexao = conectar()
    cursor = conexao.cursor()
    comando = f'DELETE FROM lista WHERE name = "{nome}"'
    cursor.execute(comando)
    conexao.commit()
    cursor.close()
    conexao.close()