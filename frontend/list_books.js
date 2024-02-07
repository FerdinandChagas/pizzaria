document.addEventListener("DOMContentLoaded", function(event) {
    event.preventDefault();
    // Fazendo uma solicitação GET para a API de categorias
    fetch('http://localhost:8000/api/books/', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            //'Authorization': 'Token ' + token
        }
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        const dadosTbody = document.getElementById("dados");
        // Verifica se o elemento com ID 'dados' existe
        if (data) {
            // Itera sobre a lista de categorias e insere cada categoria na tabela
            data.forEach(book => {
                console.log(book.id)
                const newRow = dadosTbody.insertRow();
                newRow.innerHTML = `<tr>
                                        <td>${book.id}</td>
                                        <td>${book.title}</td>
                                        <td>${book.author}</td>
                                        <td>${book.genero}</td>
                                    </tr>`;
            });
            
        } else {
            console.error("Elemento com ID 'dados' não encontrado no DOM.");
        }
    })
    .catch(error => {
        console.error('Houve um problema com a sua solicitação:', error);
    });
});
