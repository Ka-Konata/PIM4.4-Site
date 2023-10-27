# PIM4.4 Site
Um site para o PIM com integração na nossa API.
> versão do python: 3.9.10

## Indíce
* [Clonando o Repositório](#clonando-o-reposit-rio)
* [API Integration](#api-integration)
    + [Rotas que faltam integrar](#rotas-que-faltam-integrar)
    + [Funções do Modulo](#fun-es-do-modulo)
    + [Aprendendo a usar o módulo](#aprendendo-a-usar-o-m-dulo)
      - [Se conectando à API](#se-conectando-api)
      - [Fazendo login com ID e senha](#fazendo-login-com-id-e-senha)
      - [Obtendo um novo token com o refresh_token](#obtendo-um-novo-token-com-o-refresh-token)
      - [Consultando um cadastro no Banco de Dados](#consultando-um-cadastro-no-banco-de-dados)
      - [Pesquisando por uma lista de cadastros](#pesquisando-por-uma-lista-de-cadastros)
      - [Postando um novo cadastro](#postando-um-novo-cadastro)
      - [Editando um cadastro já existente](#editando-um-cadastro-j-existente)
      - [Apagando um cadastro](#apagando-um-cadastro)
    + [Modelos](#modelos)
      - [Exemplo de utilização de um modelo](#exemplo-de-utiliza-o-de-um-modelo)
    + [Lista de Modelos](#lista-de-modelos)

## Clonando o Repositório
1. Fale comigo para pegar informações sobre as variáveis de ambiente.
2. Em **"mysite/"** crie um arquivo **.env** com todas as variáveis de ambiente.
3. Caso você esteja no windows, abra um terminal como administrador e use **"Set-ExecutionPolicy Unrestricted -Force"**.
4. Crie um ambiente virtual com **"python -m venv pim4site"**
5. Ative o ambiente virtual com o comando **".\pim4site\Scripts\activate"**.
6. Instale todas as bibliotecas com o comando **"pip install -r requeriments.txt"**.
7. Vá para a pasta do servidor com **"cd mysite"**.
8. Para iniciar o servidor, use o seguinte comando **"python manage.py runserver"**.

## API Integration
### Rotas que faltam integrar
- [x] POST /api/Curso/disciplina
- [x] DELETE /api/Curso/disciplina
- [x] PUT /api/DisciplinaCursada/media/{id}
- [x] PUT /api/DisciplinaCursada/frequencia/{id}
- [x] PUT /api/DisciplinaCursada/situacao{id}
- [ ] GET /api/File/conteudo/{file}
- [ ] GET /api/File/boletim/{id}
- [ ] GET /api/File/historico/{id}
- [ ] GET /api/File/declaracao/{id}
- [ ] GET /api/File/relatorio/{id}

### Funções do Modulo
* Connection
> Classe para criar uma conexão com a API.
* Connection.login
> Função para realizar login, recebendo as informações básicas de uma conta.
* Connection.refresh
> Use quando um token estiver expirado. Ao usar o refresh_token você pode adquirir um novo token sem a necessidade de refazer o login.
* Connection.startup
> Para fazer o cadastro inicial.
* Connection.consultar
* Connection.procurar
* Connection.cadastrar
* Connection.editar
* Connection.editar
* Connection.editar
* Connection.apagar
* Connection.\[tipo de operação\].\[tipo de cadastro\]
> Substitua \[tipo de operação\] pela operação a ser realizada (ex: cadastrar ou consultar) e \[tipo de cadastro\] pelo tipo de cadastro a ser consultado, pois cada tipo tem sua própria função (ex: aluno ou conteudo).
* Connection.editar.calcular_media
> Calcula a média das notas de um cadastro do tipo "disciplina_cursada" e retorna o resultado.
* Connection.editar.calcular_frequencia
> Calcula a frequência de presença em um cadastro do tipo "disciplina_cursada" e retorna o resultado.
* Connection.editar.calcular_situacao
> Calcula a situação de aprovação em um cadastro do tipo "disciplina_cursada" e retorna o resultado
* Connection.arquivo.conteudo
* Connection.arquivo.boletim
* Connection.arquivo.declaracao
* Connection.arquivo.historico
* Connection.arquivo.relatorio
* Utils.Login.set_values_with_response
> Após instanciar um obj Login, use essa função para inserir os valores de login apartir de um obj requests.Response.
* Utils.Login.set_refresh
> Ao fazer um refresh_token, use essa função para atualziar as informações de um obj Login, inserindo o obj requests.Response obtido.
* Utils.get_file_path
> Ao fazer um request do tipo GET api/conteudo, use essa função para converter um atributo Conteudo.documento_url em um nome de arquivo válido.
* Utils.dict_to_josn
> Converte dicionários em strings json válidas.
* Utils.bytes_to_dict
> Converte bytes em dicionário.
* Utils.get_value
> Consulta um valor em um atributo requests.Response.content, returna None quando não encontrado.

### Aprendendo a usar o módulo
#### Se conectando à API:
```python
from api_integration import api, utils
conn = api.Connection("URL da API")
```
#### Fazendo login com ID e senha:
```python
# id_aluno: um número inteiro maior que 10000
response = conn.login(id_aluno, "senha da conta")

# Instanciando um login
login = utils.Login()
login.set_values_with_response(response)

# Exibe o status code do request, o token e o refresh_token
print(response.status_code, login.token, login.refresh_token)
```
#### Obtendo um novo token com o refresh_token:
```python
# id_aluno: um número inteiro maior que 10000
response = conn.refresh(id_aluno, login.token, login.refresh_token)

# Atualiza o objeto login
login.set_refresh(response)

# Verificando se o request deu certo
if login.valido == True:
    print(f"Sucesso! Novo token: {login.token}")
else:
    print("refresh_token inválido ou expirado.")
```
#### Consultando um cadastro no Banco de Dados:
```python
# id_aluno: um número inteiro maior que 10000
r, aluno = conn.consultar.aluno(login.token, id_aluno)

# Exibe o status da requisição
print(r.status_code)
```
#### Pesquisando por uma lista de cadastros:
```python
# nome_aluno: um string qualquer
r, alunos = conn.procurar.aluno(login.token, nome_aluno)

# Exibe o status da requisição
print(r.status_code)
```
#### Postando um novo cadastro:
```python
# id_curso: um número inteiro maior que 10000
curso = conn.consultar.curso(login.token, id_curso)
turma = api.Turma(
    nome="Nome da turma",
    curso=curso # Curso consultado anteriormente
)

# Enviando o cadastro
r = conn.cadastrar.turma(token, turma)

# Exibe o status da requisição
print(r.status_code)
```
#### Editando um cadastro já existente:
```python
# id_turma: um número inteiro maior que 10000
turma = conn.consultar.turma(login.token, id_turma)

# Editando o cadastro
turma.nome = "Novo nome"

# Salvando/enviando as edições feitas
r = conn.editar.turma(login.token, turma)

# Exibe o status da requisição
print(r.status_code)
```
#### Apagando um cadastro:
```python
# id_aluno: um número inteiro maior que 10000
r = conn.apagar.aluno(login.token, id_aluno)

# Exibe o status da requisição
print(r.status_code)
```

### Modelos:

#### Exemplo de utilização de um modelo:
```python
from api_integration import api
aluno = api.Aluno(
    nome="João",
    cpf=12345,
    rg=12345,
    telefone=12345,
    email="exemplo@gmail.com"
)

# Exibe os atributos da classe Aluno em formato de dicionário.
print(aluno.to_dict())
```

### Lista de Modelos
* class Pessoa
* class Aluno(Pessoa)
* class AnalistaRH(Pessoa)
* class Secretario(Pessoa)
* class Professor(Pessoa)
* class Conteudo
* class Curso_Matriculado
* class Curso
* class Disciplina_Cursada
* class Disciplina_Ministrada
* class Disciplina
* class Turma
* class Utils.Login
* class utils.Cargo
