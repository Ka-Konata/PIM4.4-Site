from api_integration import api

a = api.Aluno(
    nome="Victor",
    cpf=123,
    rg=123,
    cargo="aluno",
    telefone=123,
    email="t@gmail.com"
)

print(a.to_dict())