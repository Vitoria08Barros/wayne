from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# ================== USUÁRIOS ==================
usuarios = [
    {
        "username": "admin",
        "password": "1234",
        "nome": "Bruce Wayne",
        "role": "administrador"
    },
    {
        "username": "gerente",
        "password": "1234",
        "nome": "Lucius Fox",
        "role": "gerente"
    },
    {
        "username": "funcionario",
        "password": "1234",
        "nome": "Alfred Pennyworth",
        "role": "funcionario"
    }
]

# ================== RECURSOS ==================
recursos = [
    {
        "id": 1,
        "nome": "Batmobile X-7",
        "tipo": "Veículo",
        "status": "Ativo",
        "quantidade": 1
    },
    {
        "id": 2,
        "nome": "Drone de Vigilância Mark IV",
        "tipo": "Equipamento",
        "status": "Ativo",
        "quantidade": 12
    },
    {
        "id": 3,
        "nome": "Sistema de Câmeras Infravermelhas",
        "tipo": "Dispositivo de Segurança",
        "status": "Ativo",
        "quantidade": 48
    }
]

# ================== LOGIN ==================
@app.route('/login', methods=['POST'])
def login():
    data = request.json

    for user in usuarios:
        if user['username'] == data.get('username') and user['password'] == data.get('password'):
            return jsonify(user)

    return jsonify({"erro": "Usuário inválido"}), 401


# ================== LISTAR RECURSOS ==================
@app.route('/recursos', methods=['GET'])
def get_recursos():
    return jsonify(recursos)


# ================== ADICIONAR RECURSO ==================
@app.route('/recursos', methods=['POST'])
def add_recurso():
    data = request.json

    novo = {
        "id": len(recursos) + 1,
        "nome": data.get('nome'),
        "tipo": data.get('tipo'),
        "status": data.get('status'),
        "quantidade": data.get('quantidade')
    }

    recursos.append(novo)
    return jsonify(novo)


# ================== ATUALIZAR RECURSO ==================
@app.route('/recursos/<int:id>', methods=['PUT'])
def update_recurso(id):
    data = request.json

    for r in recursos:
        if r['id'] == id:
            r['nome'] = data.get('nome', r['nome'])
            r['tipo'] = data.get('tipo', r['tipo'])
            r['status'] = data.get('status', r['status'])
            r['quantidade'] = data.get('quantidade', r['quantidade'])
            return jsonify(r)

    return jsonify({"erro": "Recurso não encontrado"}), 404


# ================== DELETAR RECURSO ==================
@app.route('/recursos/<int:id>', methods=['DELETE'])
def delete_recurso(id):
    global recursos

    recursos = [r for r in recursos if r['id'] != id]
    return jsonify({"msg": "Recurso deletado com sucesso"})


# ================== INICIAR SERVIDOR ==================
if __name__ == '__main__':
    app.run(debug=True)
