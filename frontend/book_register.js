document.getElementById('book_register').addEventListener('submit', function(event) {
    event.preventDefault();

    var local_title = document.getElementById('title').value;
    var local_author = document.getElementById('author').value;
    var local_genero = document.getElementById('genero').value;

    // Fazendo uma solicitação POST para a API de autenticação
    fetch('http://localhost:8000/api/books/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            //'Authorization': 'Token ' + token
        },
        body: JSON.stringify({
            title: local_title,
            author: local_author,
            genero: local_genero
        })
    })
    .then(data => {
        if(data){
            window.location.href = 'index2.html';
            alert("Cadastro realizado com sucesso!");
        }
    })
    .catch(error => {
        console.error('Falha ao realizar a requisição:', error);
    });
});
