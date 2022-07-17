function fazPost(url, body) {
    console.log("Body=", body)
    let request = new XMLHttpRequest()
    request.open("POST", url, true)
    request.setRequestHeader("Content-type", "application/json")
    request.send(JSON.stringify(body))

    request.onload = function() {
        if(this.status == 201){
            alert('Sucesso!')
        }
        console.log(this.responseText)
    }

    return request.responseText
}


function cadastraCliente() {
    event.preventDefault()
    let url = "http://127.0.0.1:8000/v1/clientes/"
    let nome = document.getElementById("nome").value
    let telefone = document.getElementById("telefone").value
    let endereco = document.getElementById("endereco").value
    let tipo = document.getElementById("tipo").value

    body = {
        "nome": nome,
        "telefone": telefone,
        "endereco": endereco,
        "tipo": tipo
    
    }

    fazPost(url, body)
}

function fazGet(url) {
    let request = new XMLHttpRequest()
    request.open("GET", url, false)
    request.send(null)
    return request.responseText
}

function criaLinha(cliente) {
    console.log(cliente)
    linha = document.createElement("tr");
    tdId = document.createElement("td");
    tdNome = document.createElement("td");
    tdId.innerHTML = cliente.nome
    tdNome.innerHTML = cliente.endereco

    linha.appendChild(tdId);
    linha.appendChild(tdNome);

    return linha;
}

function main() {
    let data = fazGet("http://127.0.0.1:8000/v1/clientes/");
    let clientes = JSON.parse(data);
    let tabela = document.getElementById("tabela");
    clientes.results.forEach(element => {
        let linha = criaLinha(element);
        tabela.appendChild(linha);
    });
    // Para cada cliente
        // criar uma linha
        // adicionar na tabela
}

main()