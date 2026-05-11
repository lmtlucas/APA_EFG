class Curso:
    def __init__(self, dados):
        self.dados = dados

        self.id = dados["id"]
        self.nome_curso = dados["nome_curso"]
        self.instituicao = dados["instituicao"]
        self.categoria = dados["categoria"]
        self.area = dados["area"]
        self.modalidade = dados["modalidade"]
        self.idade_minima = dados["idade_minima"]
        self.carga_horaria = dados["carga_horaria"]
        self.status = dados["status"]
        self.link = dados["link"]
        self.descricao = dados["descricao"]

    def corresponde_a_busca(self, busca):
        return busca in self.nome_curso.lower()

    def corresponde_a_categoria(self, categoria):
        return categoria == "" or categoria == self.categoria

    def corresponde_a_modalidade(self, modalidade):
        return modalidade == "" or modalidade == self.modalidade

    def para_dict(self):
        return self.dados
