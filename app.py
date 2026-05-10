from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/")
def home():

    with open("cursos.json", "r", encoding="utf-8") as arquivo:
        cursos = json.load(arquivo)

    return render_template(
        "cursos.html",
        cursos=cursos
    )

app.run(debug=True)
