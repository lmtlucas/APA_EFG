class Curso:
    def __init__(self, id, titulo, instituicao, categoria, localizacao, modalidade, status, descricao, link):
        self.id = id
        self.titulo = titulo
        self.instituicao = instituicao
        self.categoria = categoria
        self.localizacao = localizacao
        self.modalidade = modalidade
        self.status = status
        self.descricao = descricao
        self.link = link

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "instituicao": self.instituicao,
            "categoria": self.categoria,
            "localizacao": self.localizacao,
            "modalidade": self.modalidade,
            "status": self.status,
            "descricao": self.descricao,
            "link": self.link
        }
