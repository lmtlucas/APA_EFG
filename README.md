# Portal de Cursos Gratuitos GO

## Sobre o projeto

Este projeto foi criado com o objetivo de centralizar cursos gratuitos disponíveis em Goiânia e região.

Hoje, essas oportunidades estão espalhadas em vários sites (como EFG, IFG, Senai, etc), o que dificulta encontrar cursos abertos.

A ideia desse portal é facilitar o acesso, reunindo tudo em um só lugar.

### Sobre os dados dos cursos
Nesta primeira versão, os cursos estão sendo cadastrados manualmente no arquivo `cursos.json`.

Como próximo passo, a ideia é estudar o uso de web scraping para buscar informações diretamente dos sites das instituições, tornando o processo de atualização mais rápido e eficiente.

---

## O que foi desenvolvido até agora

Nesta primeira versão (MVP inicial), foram implementadas as seguintes funcionalidades:

* Estrutura básica do projeto com Flask
* Criação de uma API simples
* Leitura de dados a partir de um arquivo JSON (`cursos.json`)
* Exibição dos cursos na tela usando JavaScript
* Organização do código utilizando Programação Orientada a Objetos (POO)

---

## Como o projeto funciona

O fluxo do projeto é simples:

```txt
cursos.json → Flask → API → JavaScript → HTML (tela)
```

### Explicando:

* O arquivo `cursos.json` guarda os dados dos cursos
* O Flask lê esse arquivo
* O Flask cria uma rota `/api/cursos` que retorna esses dados
* O JavaScript busca esses dados usando `fetch`
* O HTML exibe os cursos na tela em formato de lista

---

## Organização com POO

Após aprender Python intermediário e POO, refatoramos o projeto para melhorar sua organização.

Inicialmente, validamos o funcionamento da aplicação com dados vindos do `cursos.json`. Em seguida, aplicamos POO criando:

- `Curso` → representa um curso individual
- `RepositorioCursos` → responsável por carregar e organizar os cursos

### Para adicionar um novo detalhe ao curso:

- Adicionar o atributo na classe `Curso` (`__init__`)
- Incluir no método `to_dict`
- Ajustar o carregamento na classe `RepositorioCursos`
- Exibir no `script.js`

Isso facilita a evolução do projeto sem bagunçar o código.

## Estrutura do projeto

```txt
portal-cursos-go/
│
├── app.py
├── cursos.json
├── requirements.txt
│
├── models/ │
|   └── curso.py
│
├── repositories/
│   └── repositorio_cursos.py
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    └── script.js
```

---

## Tecnologias utilizadas

* Python
* Flask
* HTML
* CSS
* JavaScript

---

## Como rodar o projeto

1. Criar ambiente virtual:

```bash
python -m venv venv
```

2. Ativar ambiente virtual:

```bash
venv\Scripts\activate
```

3. Instalar dependências:

```bash
pip install -r requirements.txt
```

4. Rodar o projeto:

```bash
python app.py
```

5. Acessar no navegador:

```
http://127.0.0.1:5000
```

---

## Próximos passos

* Aplicar um visual mais organizado usando Tailwind CSS
* Melhorar o layout dos cards dos cursos
* Adicionar filtro por categoria
* Adicionar filtro por modalidade
* Criar seção de FAQ
* Otimizar a busca de dados dos cursos usando web scraping
* Estudar formas de atualizar os dados automaticamente a partir dos sites das instituições

---

## Observação

O projeto está sendo desenvolvido com apoio dos professores do curso e com base nos conhecimentos adquiridos até o momento, principalmente na linguagem Python.

---
