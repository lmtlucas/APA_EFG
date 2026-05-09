from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route("/api/cursos")
def listar_cursos():

    with open("cursos.json", "r", encoding="utf-8") as arquivo:
        cursos = json.load(arquivo)

    print("Cursos carregados!")

    return jsonify(cursos)

app.run(debug=True)
