from flask import Flask, jsonify
from flask import request
import pymysql
import pymysql.cursors
from flask_cors import CORS

#Conexão Banco de Dados
db = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='api_crud',
    cursorclass=pymysql.cursors.DictCursor
)

app = Flask(__name__)
CORS(app)

#GET todas as pessoas
@app.route("/pessoas", methods=["GET"])
def ler_pessoas():
    cursor = db.cursor()

    cursor.execute("SELECT * FROM pessoas")
    pessoas = cursor.fetchall()
    cursor.close()
    return jsonify(pessoas)

#GET pessoa por id
@app.route("/pessoas/<id_pessoa>", methods=['GET'])
def consultar_pessoa_por_id(id_pessoa):
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM pessoas where id = {id_pessoa}")
    pessoa = cursor.fetchone()
    cursor.close()
    if pessoa is None:
        return f'Não existe pessoa com o id {id_pessoa} cadastrada no banco de dados.'
    return jsonify(pessoa)


#POST criando cadastro de uma nova pessoa
@app.route("/pessoas", methods=["POST"])
def criar_pessoas():
    cursor = db.cursor()
    body = request.get_json()
    cursor.execute(f"""
    INSERT INTO pessoas (nome_completo, data_nascimento, endereço, cpf, estado_civil)
    VALUE ('{body['nome_completo']}', '{body['data_nascimento']}', '{body['endereço']}', '{body['cpf']}', '{body['estado_civil']}')
    """)
    db.commit()
    return "Criando novo cadastro"

#PUT atualizando pessoa por id
@app.route("/pessoas/<id_pessoa>", methods=["PUT"])
def atualizar_pessoas(id_pessoa):
    cursor = db.cursor()
    body = request.get_json()
    cursor.execute(f"""
    UPDATE pessoas
    SET cpf = '{body['cpf']}',
    nome_completo = '{body['nome_completo']}',
    data_nascimento = '{body['data_nascimento']}',
    endereço = '{body['endereço']}',
    estado_civil = '{body['estado_civil']}' 
    where id = {id_pessoa};
    """)

    db.commit()

    return f"CADASTRO ATUALIZADO {id_pessoa}"

#DELETE deletando pessoa por id
@app.route("/pessoas/<id_pessoa>", methods=['DELETE'])
def deletar_pessoas(id_pessoa):
    cursor = db.cursor()
    cursor.execute(f"""
    DELETE FROM pessoas
    where id = {id_pessoa};
    """)
    db.commit()

    return f"Deletando Pessoa {id_pessoa}"

#Início da API
if __name__ == '__main__':
    app.run(debug=True)