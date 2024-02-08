document.addEventListener("DOMContentLoaded", function(event) {
    event.preventDefault();
    // Fazendo uma solicitação GET para a API de categorias
    fetch('http://localhost:8000/api/pizzas/', {
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
            // Itera sobre a lista de pizzas e insere cada pizza na tabela
            data.forEach(pizza => {

                const newRow = dadosTbody.insertRow();
                newRow.innerHTML = `<tr>
                                        <td>${pizza.id}</td>
                                        <td>${pizza.flavor}</td>
                                        <td>${pizza.price}</td>
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
