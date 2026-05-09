import requests
from bs4 import BeautifulSoup
import re
import json


url = "https://efg.org.br/cursos"

resposta = requests.get(url)

if resposta.status_code == 200:
    print("Página carregada com sucesso!")

    soup = BeautifulSoup(resposta.text, "html.parser")

    cards = soup.find_all("div", class_="col-md-4")

    cursos = []

    for indice, card in enumerate(cards, start=1):
        titulos = card.find_all("div", class_="ccc-titulo")

        categoria = None
        titulo = None

        if len(titulos) >= 2:
            categoria = titulos[0].text.strip()
            titulo = titulos[1].text.strip()

        outros_detalhes = card.find("div", class_="ccc-outros")

        idade_minima = None
        carga_horaria = None

        if outros_detalhes:
            spans = outros_detalhes.find_all("span")

            for span in spans:
                texto = span.text.strip()
                numero = re.search(r"\d+", texto)

                if "+" in texto and numero:
                    idade_minima = int(numero.group())

                elif "h" in texto.lower() and numero:
                    carga_horaria = int(numero.group())

        botao = card.find("a", class_="btn btn-insc-disponivel")

        link = None

        if botao:
            onclick = botao.get("onclick")

            if onclick:
                numero = re.search(r"\d+", onclick)

                if numero:
                    turma_id = numero.group()
                    link = f"https://efg.org.br/detalhes-turma?codigo={turma_id}"

        curso = {
            "id": indice,
            "titulo": titulo,
            "instituicao": {
                "nome": "EFG",
                "unidade": None,
                "cidade": None
            },
            "categoria": categoria,
            "area": None,
            "modalidades": [],
            "turnos": [],
            "idade_minima": idade_minima,
            "carga_horaria": carga_horaria,
            "status": "Aberto",
            "link": link,
            "descricao": None
        }

        cursos.append(curso)

    with open("cursos.json", "w", encoding="utf-8") as arquivo:
        json.dump(cursos, arquivo, ensure_ascii=False, indent=2)

    print(f"{len(cursos)} cursos salvos em cursos.json")

else:
    print(f"Erro ao acessar a página. Código: {resposta.status_code}")
