import mysql.connector
from flask import Flask, request, jsonify
from flask_cors import CORS

# ================== CONEXÃO ==================
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sara280957.",  
        database="wayne_db"
    )

app = Flask(__name__)
CORS(app)

# ================== LOGIN ==================
@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.json

        print("DADOS RECEBIDOS:", data)

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        # 🔥 busca só pelo username (melhor prática pra debug)
        query = "SELECT * FROM usuarios WHERE username = %s"
        cursor.execute(query, (data.get('username').strip(),))

        user = cursor.fetchone()

        print("USUÁRIO DO BANCO:", user)

        cursor.close()
        conn.close()

        # valida senha no Python
        if user and user['password'] == data.get('password').strip():
            return jsonify(user)

        return jsonify({"erro": "Usuário inválido"}), 401

    except Exception as e:
        print("ERRO NO LOGIN:", e)
        return jsonify({"erro": str(e)}), 500


# ================== LISTAR RECURSOS ==================
@app.route('/recursos', methods=['GET'])
def get_recursos():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM recursos")
    dados = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(dados)


# ================== ADICIONAR RECURSO ==================
@app.route('/recursos', methods=['POST'])
def add_recurso():
    role = request.headers.get('role')

    if role != 'administrador':
        return jsonify({"erro": "Acesso negado"}), 403

    data = request.json

    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO recursos (nome, tipo, status, quantidade)
    VALUES (%s, %s, %s, %s)
    """

    cursor.execute(query, (
        data.get('nome'),
        data.get('tipo'),
        data.get('status'),
        data.get('quantidade')
    ))

    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({"msg": "Recurso adicionado com sucesso"})


# ================== ATUALIZAR RECURSO ==================
@app.route('/recursos/<int:id>', methods=['PUT'])
def update_recurso(id):
    role = request.headers.get('role')

    if role != 'administrador':
        return jsonify({"erro": "Acesso negado"}), 403

    data = request.json

    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
    UPDATE recursos
    SET nome=%s, tipo=%s, status=%s, quantidade=%s
    WHERE id=%s
    """

    cursor.execute(query, (
        data.get('nome'),
        data.get('tipo'),
        data.get('status'),
        data.get('quantidade'),
        id
    ))

    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({"msg": "Atualizado com sucesso"})


# ================== DELETAR RECURSO ==================
@app.route('/recursos/<int:id>', methods=['DELETE'])
def delete_recurso(id):
    role = request.headers.get('role')

    if role != 'administrador':
        return jsonify({"erro": "Acesso negado"}), 403

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM recursos WHERE id = %s", (id,))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({"msg": "Recurso deletado com sucesso"})


# ================== START ==================
if __name__ == '__main__':
    app.run(debug=True)
