// Função para redirecionar para a página de edição de cadastro ao clicar em um item na lista de resultados
function redirect_to_cad(tipo, id) {
    if (id != null) {
        window.location = tipo + "?id=" + id
    } else {
        window.location = tipo
    }
}