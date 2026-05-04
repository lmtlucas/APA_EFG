from flask import Flask, jsonify, render_template
from repositories.repositorio_cursos import RepositorioCursos

app = Flask(__name__)

repositorio = RepositorioCursos("cursos.json")


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/api/cursos")
def listar_cursos():
    cursos = repositorio.listar_como_dict()
    return jsonify(cursos)


if __name__ == "__main__":
    app.run(debug=True)
