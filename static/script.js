fetch("/api/cursos")
  .then(response => response.json())
  .then(cursos => {
    const lista = document.getElementById("lista-cursos");

    cursos.forEach(curso => {
      const card = document.createElement("div");

      card.innerHTML = `
        <h2>${curso.titulo}</h2>
        <p>${curso.instituicao}</p>
        <p>${curso.categoria}</p>
        <p>${curso.modalidade}</p>
        <a href="${curso.link}" target="_blank">Ver curso</a>
      `;

      lista.appendChild(card);
    });
  });
