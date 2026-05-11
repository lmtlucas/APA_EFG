# Portal de Cursos Gratuitos GO

## Sobre o projeto

Este projeto foi criado com o objetivo de centralizar cursos gratuitos disponíveis em Goiânia e região.

Hoje, essas oportunidades estão espalhadas em vários sites (como EFG, IFG, Senai, etc.), o que dificulta encontrar cursos abertos.

A ideia deste portal é facilitar o acesso, reunindo tudo em um só lugar.

---

## Sobre os dados dos cursos

Os cursos são lidos a partir do arquivo `cursos.json`.

Esse arquivo pode ser preenchido manualmente ou atualizado por meio do scraper desenvolvido para coletar dados do site da EFG. No entanto, o scraper não é executado automaticamente quando o portal é iniciado.

Ou seja, o fluxo atual é:

```text
Scraper → cursos.json → Flask → HTML
```

O Flask é responsável por ler os dados salvos no JSON e exibir os cursos no portal.

---

## Sobre a coleta de dados

A coleta de dados do portal foi desenvolvida utilizando técnicas de web scraping com as bibliotecas `requests` e `BeautifulSoup`.

O objetivo é facilitar a identificação de cursos com inscrições abertas e organizar as informações necessárias para exibição no sistema.

Durante a análise do site da EFG, foi percebido que algumas informações importantes não apareciam diretamente no HTML inicial da página, pois determinados elementos eram carregados dinamicamente.

Após pesquisas e testes, a solução adotada foi reconstruir algumas URLs dinamicamente a partir dos dados disponíveis na estrutura da página.

O scraper é responsável apenas por coletar e atualizar os dados quando executado manualmente pelo desenvolvedor.

Após a coleta, os dados são armazenados no arquivo `cursos.json`, que posteriormente é utilizado pelo Flask para exibição dos cursos no portal.

O uso do JSON foi escolhido para:

- organizar os dados de forma estruturada;
- facilitar a leitura das informações pelo Flask;
- simplificar filtros e futuras buscas;
- evitar informações escritas manualmente no código;
- separar a coleta de dados da interface do sistema;
- preparar o projeto para futuras integrações com banco de dados.

O JavaScript não é a principal tecnologia utilizada no projeto. O foco da aplicação está no uso de Python com Flask para estrutura da aplicação e manipulação dos dados. O JavaScript poderá ser utilizado apenas em funcionalidades específicas, quando necessário.

---

## O que foi desenvolvido até agora

Nesta primeira versão (MVP inicial), foram implementadas as seguintes funcionalidades:

- Estrutura básica do projeto com Flask;
- Criação de uma API simples;
- Leitura de dados a partir de um arquivo JSON (`cursos.json`);
- Exibição dos cursos na tela;
- Organização do código utilizando Programação Orientada a Objetos (POO);
- Desenvolvimento inicial do scraper da EFG.

---

## Como o projeto funciona

O fluxo atual do projeto é simples:

```text
cursos.json → Flask → Templates HTML
```

### Explicando:

- O arquivo `cursos.json` armazena os dados dos cursos;
- O Flask lê esse arquivo;
- As informações são enviadas para os templates HTML;
- Os cursos são exibidos na tela em formato de cards.

---

## Organização com POO

Após aprender Python intermediário e POO, o projeto foi refatorado para melhorar sua organização.

Inicialmente, foi validado o funcionamento da aplicação utilizando dados vindos do `cursos.json`. Em seguida, foi aplicada Programação Orientada a Objetos criando:

- `Curso` → representa um curso individual;
- `RepositorioCursos` → responsável por carregar e organizar os cursos.

### Para adicionar um novo detalhe ao curso:

- Adicionar o atributo na classe `Curso` (`__init__`);
- Incluir no método `to_dict`;
- Ajustar o carregamento na classe `RepositorioCursos`;
- Exibir a informação no template HTML.

Isso facilita a evolução do projeto sem desorganizar o código.

---

## Estrutura do projeto

```text
portal-cursos-go/
│
├── app.py
├── cursos.json
├── requirements.txt
│
├── models/
│   └── curso.py
│
├── repositories/
│   └── repositorio_cursos.py
│
├── scrapers/
│   └── scraper_efg.py
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

---

## Tecnologias utilizadas

- Python
- Flask
- HTML
- CSS
- JSON
- Requests
- BeautifulSoup
- JavaScript (apenas quando necessário)

---

## Como rodar o projeto

### 1. Criar ambiente virtual

```bash
python -m venv venv
```

### 2. Ativar ambiente virtual

```bash
venv\Scripts\activate
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Rodar o projeto

```bash
python app.py
```

### 5. Acessar no navegador

```text
http://127.0.0.1:5000
```

---

## Próximos passos

- Estudar formas de atualização dos dados no futuro.

---

## Observação

O projeto está sendo desenvolvido com apoio dos professores do curso e com base nos conhecimentos adquiridos até o momento, principalmente na linguagem Python.
