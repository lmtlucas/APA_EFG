from flask import Flask, render_template, request
import json

app = Flask(__name__)

def carregar_cursos():
    with open("cursos.json", "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)

@app.route("/")
def home():
    cursos = carregar_cursos()

    cursos_recentes = cursos[:9]

    return render_template(
        "index.html",
        cursos_recentes=cursos_recentes
    )


@app.route("/cursos")
def listar_cursos():
    cursos = carregar_cursos()

    # Filtrar cursos com base nos parâmetros de busca, categoria e modalidade
    busca = request.args.get("busca", "").lower()
    categoria = request.args.get("categoria", "")
    modalidade = request.args.get("modalidade", "")

    cursos_filtrados = []
    for curso in cursos:
        nome_curso = curso["nome_curso"].lower()
        categoria_curso = curso["categoria"]
        modalidades_curso = curso["modalidades"]

        busca_ok = busca in nome_curso
        categoria_ok = categoria == "" or categoria == categoria_curso
        modalidade_ok = modalidade == "" or modalidade in modalidades_curso

        if busca_ok and categoria_ok and modalidade_ok:
            cursos_filtrados.append(curso)

    return render_template(
        "cursos.html",
        cursos=cursos_filtrados,
        busca=busca,
        categoria=categoria,
        modalidade=modalidade
    )


app.run(debug=True)
