from flask import Flask, jsonify, request
from src.business.cadastro_cliente import CadastroCliente
from src.entities.pessoa_fisica import PessoaFisica

app = Flask(__name__)

cadastro_cliente = CadastroCliente()


@app.route("/cliente", methods=['POST'])
def inserir_cliente():
    dados = request.json

    cliente = PessoaFisica(dados['id'], dados['endereco'], dados['telefone'], dados['cpf'], dados['nome'])
    cadastro_cliente.inserir(cliente)

    return "ok", 201

@app.route("/cliente")
def consultar_clientes():
    resultado = cadastro_cliente.listar_todos()  

    return jsonify(resultado[0].__dict__)
