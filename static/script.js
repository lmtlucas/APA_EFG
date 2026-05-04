fetch('/api/cursos')
  .then((response) => response.json())
  .then((cursos) => {
    const lista = document.getElementById('lista-cursos');

    cursos.forEach((curso) => {
      const card = document.createElement('div');

card.innerHTML = `
  <h2>${curso.titulo}</h2>
  <p><strong>Instituição:</strong>
    ${curso.instituicao.nome} - ${curso.instituicao.unidade}
  </p>
  <p><strong>Cidade:</strong> ${curso.instituicao.cidade}</p>
  <p><strong>Nível:</strong> ${curso.nivel}</p>
  <p><strong>Área:</strong> ${curso.area}</p>
  <p><strong>Modalidades:</strong> ${curso.modalidades.join(", ")}</p>
  <p><strong>Idade mínima:</strong> ${curso.idade_minima} anos</p>
  <p><strong>Carga horária:</strong> ${curso.carga_horaria}h</p>
  <p><strong>Status:</strong> ${curso.status}</p>
  <p><strong>Descrição:</strong> ${curso.descricao}</p>
  <a href="${curso.link}" target="_blank">Ver curso</a>
`;

      lista.appendChild(card);
    });
  });
