import json
from models.curso import Curso

class CursoRepository:
    def __init__(self, caminho_arquivo="cursos.json"):
        self.caminho_arquivo = caminho_arquivo

    def carregar_todos(self):
        with open(self.caminho_arquivo, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

        return [Curso(curso) for curso in dados]

    def listar_recentes(self, quantidade=9):
        cursos = self.carregar_todos()
        return [curso.para_dict() for curso in cursos[:quantidade]]

    def filtrar(self, busca="", categoria="", area="", modalidade=""):
        cursos = self.carregar_todos()

        cursos_filtrados = []

        for curso in cursos:
            busca_ok = curso.corresponde_a_busca(busca)
            categoria_ok = curso.corresponde_a_categoria(categoria)
            area_ok = curso.corresponde_a_area(area)
            modalidade_ok = curso.corresponde_a_modalidade(modalidade)

            if busca_ok and categoria_ok and area_ok and modalidade_ok:
                cursos_filtrados.append(curso.para_dict())

        return cursos_filtrados
