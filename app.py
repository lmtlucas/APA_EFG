from flask import Flask, jsonify, render_template
import json

app = Flask(__name__)

def carregar_cursos():
    with open("cursos.json", "r", encoding="utf-8") as arquivo:
        cursos = json.load(arquivo)
    return cursos

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/api/cursos")
def listar_cursos():
    cursos = carregar_cursos()
    return jsonify(cursos)

if __name__ == "__main__":
    app.run(debug=True)
