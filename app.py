from flask import Flask, jsonify, request
from marshmallow import Schema, fields, ValidationError, validate

# Instância da classe Flask
app = Flask(__name__)

class LoginSchema(Schema):
    email = fields.Email(required=True)
    password = fields.String(required=True, validate=validate.Length(min=8, max=64))

class RegisterSchema(Schema):
    name = fields.String(required=True, validate=validate.Length(min=1, max=32))
    email = fields.Email(required=True)
    password = fields.String(required=True, validate=validate.Length(min=8, max=64))

@app.route("/login", methods=["POST"])
def login():
    try:
        # Valida os dados
        result = LoginSchema().load(request.json)

    except ValidationError as err:

        # Erro na validação dos campos
        return jsonify(err.messages), 400

    # Examplo envia a saida de volta
    return jsonify(result), 200

@app.route("/register", methods=["POST"])
def register():
    try:
        # Valida os dados
        result = RegisterSchema().load(request.json)

    except ValidationError as err:

        # Erro na validação dos campos
        return jsonify(err.messages), 400

    # Examplo envia a saida de volta
    return jsonify(result), 200