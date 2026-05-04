import json

from models.curso import Curso

class RepositorioCursos:
    def __init__(self, caminho_arquivo):
        self.caminho_arquivo = caminho_arquivo

    def carregar_todos(self):
        with open(self.caminho_arquivo, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

        cursos = []

        for item in dados:
            curso = Curso(
                item["id"],
                item["titulo"],
                item["instituicao"],
                item["nivel"],
                item["area"],
                item["modalidades"],
                item["idade_minima"],
                item["carga_horaria"],
                item["status"],
                item["descricao"],
                item["link"]
            )

            cursos.append(curso)

        return cursos

    def listar_como_dict(self):
        cursos = self.carregar_todos()

        return [curso.to_dict() for curso in cursos]
