class Curso:
    def __init__(self, id, titulo, instituicao, nivel, area, modalidades, idade_minima, carga_horaria, status, descricao, link):
        self.id = id
        self.titulo = titulo
        self.instituicao = instituicao
        self.nivel = nivel
        self.area = area
        self.modalidades = modalidades
        self.idade_minima = idade_minima
        self.carga_horaria = carga_horaria
        self.status = status
        self.descricao = descricao
        self.link = link

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "instituicao": self.instituicao,
            "nivel": self.nivel,
            "area": self.area,
            "modalidades": self.modalidades,
            "idade_minima": self.idade_minima,
            "carga_horaria": self.carga_horaria,
            "status": self.status,
            "descricao": self.descricao,
            "link": self.link
        }
