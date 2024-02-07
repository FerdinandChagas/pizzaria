document.getElementById('pizza_register').addEventListener('submit', function(event) {
    event.preventDefault();

    var local_flavor = document.getElementById('flavor').value;
    var local_size = document.getElementById('size').value;
    var local_border = document.getElementById('border').value;
    var local_border_flavor = document.getElementById('border_flavor').value;
    var local_price = document.getElementById('price').value;
    var local_sweet = document.getElementById('sweet').value;

    // Fazendo uma solicitação POST para a API de autenticação
    fetch('http://localhost:8000/api/pizzas/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            //'Authorization': 'Token ' + token
        },
        body: JSON.stringify({
            flavor: local_flavor,
            size: local_size,
            border: local_border,
            border_flavor: local_border_flavor,
            price: local_price,
            sweet: local_sweet
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
