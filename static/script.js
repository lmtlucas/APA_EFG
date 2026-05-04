fetch('/api/cursos')
  .then((response) => response.json())
  .then((cursos) => {
    const lista = document.getElementById('lista-cursos');

    cursos.forEach((curso) => {
      const card = document.createElement('div');

      card.innerHTML = `
  <h2>${curso.titulo}</h2>
  <p><strong>Instituição:</strong> ${curso.instituicao}</p>
  <p><strong>Categoria:</strong> ${curso.categoria}</p>
  <p><strong>Localização:</strong> ${curso.localizacao}</p>
  <p><strong>Modalidade:</strong> ${curso.modalidade}</p>
  <p><strong>Status:</strong> ${curso.status}</p>
  <p><strong>Descrição:</strong> ${curso.descricao}</p>
  <a href="${curso.link}" target="_blank">Ver curso</a>
`;

      lista.appendChild(card);
    });
  });
