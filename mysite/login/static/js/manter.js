// Função para redirecionar para a página de edição de cadastro ao clicar em um item na lista de resultados
function redirect_to_cad(tipo, id) {
    if (id != null) {
        window.location = tipo + "?id=" + id
    } else {
        window.location = tipo
    }
}

function alunos_em_disciplina(tipo, disciplina, curso, filtro) {
    input = document.getElementById("filtro")
    if (filtro == true && input.value != undefined) {
        window.location = tipo + "?disciplina=" + disciplina + "&curso=" + curso + "&filtro=" + input.value
    } else {
        window.location = tipo + "?disciplina=" + disciplina + "&curso=" + curso + "&filtro="
    }
}

function atualizar_obj(tipo, id) {
    url = tipo + "?id=" + id
    let valores = document.getElementsByClassName("input")
    for(let i = 0; i < valores.length; i++) {
        url = url + "&" + valores[i].id + "=" + valores[i].value
    }
}