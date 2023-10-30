import os, json
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from api_integration import api, utils
from login.views import is_logged, set_cookies

conn = api.Connection(os.environ["API_URL"])

def check_login(request: HttpRequest) -> [dict, api.Login]:
    # Verificando se o usuário está logado.
    logged, login = is_logged(request)
    if not logged:
        return redirect("login:index"), login

    # Fazendo o request na API
    response, secretario = conn.consultar.secretario(login.token, login.id)
    context = {
        "erros":[]
    }

    # Caso o token esteja expirado.
    if response.status_code == 401:
        # Verificando se o refresh_token é válido
        refresh = conn.refresh(login.id, login.token, login.refresh_token)
        if refresh.status_code == 400:
            return redirect("login:index"), login
        
        # Caso o refresh tenha tido êxito
        login = api.Login()
        login.set_values_with_response(refresh)
        # Fazendo o request na API novamente com o novo token
        response, secretario = conn.consultar.secretario(login.token, login.id)

    # Caso o token seja válido, mas o usuário não tenha permissão para usar o endpoint.
    elif response.status_code == 403 or login.cargo != utils.Cargo.SECRETARIO:
        return redirect("erros:403"), login
    
    # Caso tudo ocorra bem
    context["secretario"] = secretario
    return context, login

# Create your views here.
def index(request: HttpRequest):
    """Página inicial da área do secretario de RH"""
    context, login = check_login(request)
    if not isinstance(context, dict):
        return context

    # Adicionando o obj ao contexto e respondendo o request.
    return set_cookies(render(request, "secretario/index.html", context), login)

def procurar_aluno(request: HttpRequest):
    """Página inicial para buscas de aluno"""
    context, login = check_login(request)
    if not isinstance(context, dict):
        return context
    
    filtro = request.GET.get("filtro", "")
    response, alunos = conn.procurar.aluno(login.token, filtro)
    context["resultados"] = alunos
    
    # Adicionando o obj ao contexto e respondendo o request.
    return set_cookies(render(request, "secretario/manter_aluno.html", context), login)

def procurar_curso(request: HttpRequest):
    """Página inicial para buscas de curso"""
    context, login = check_login(request)
    if not isinstance(context, dict):
        return context
    
    filtro = request.GET.get("filtro", "")
    response, cursos = conn.procurar.curso(login.token, filtro)
    context["resultados"] = cursos
    
    # Adicionando o obj ao contexto e respondendo o request.
    return set_cookies(render(request, "secretario/manter_curso.html", context), login)

def procurar_turma(request: HttpRequest):
    """Página inicial para buscas de turma"""
    context, login = check_login(request)
    if not isinstance(context, dict):
        return context
    
    filtro = request.GET.get("filtro", "")
    response, turmas = conn.procurar.turma(login.token, filtro)
    context["resultados"] = turmas
    
    # Adicionando o obj ao contexto e respondendo o request.
    return set_cookies(render(request, "secretario/manter_turma.html", context), login)

def procurar_disciplina(request: HttpRequest):
    """Página inicial para buscas de disciplina"""
    context, login = check_login(request)
    if not isinstance(context, dict):
        return context
    
    filtro = request.GET.get("filtro", "")
    response, disciplinas = conn.procurar.disciplina(login.token, filtro)
    context["resultados"] = disciplinas
    
    # Adicionando o obj ao contexto e respondendo o request.
    return set_cookies(render(request, "secretario/manter_disciplina.html", context), login)

def __editar(request: HttpRequest, funcao, path):
    context, login = check_login(request)
    if not isinstance(context, dict):
        return context
    
    id = request.GET.get("id", "")
    if id != "":
        response, obj = funcao(login.token, id)
        context["cadastro"] = obj
    else:
        context["cadastro"] = None

    # Adicionando o obj ao contexto e respondendo o request.
    return set_cookies(render(request, path, context), login)

def editar_aluno(request: HttpRequest):
    """Página para cadastro ou alteração de cadastro de aluno"""
    return __editar(request, conn.consultar.aluno, "secretario/info_aluno.html")

def editar_curso(request: HttpRequest):
    """Página para cadastro ou alteração de cadastro de curso"""
    return __editar(request, conn.consultar.curso, "secretario/info_curso.html")

def editar_turma(request: HttpRequest):
    """Página para cadastro ou alteração de cadastro de turma"""
    return __editar(request, conn.consultar.turma, "secretario/info_turma.html")

def editar_disciplina(request: HttpRequest):
    """Página para cadastro ou alteração de cadastro de disciplina"""
    return __editar(request, conn.consultar.disciplina, "secretario/info_disciplina.html")

def procurar_professor_em_turma(request: HttpRequest):
    """Página inicial para buscas de disciplina_ministrada"""
    context, login = check_login(request)
    if not isinstance(context, dict):
        return context
    
    filtro = request.GET.get("filtro", "")
    response, disciplina_ministrada = conn.procurar.disciplina_ministrada(login.token, filtro)
    context["resultados"] = disciplina_ministrada
    
    # Adicionando o obj ao contexto e respondendo o request.
    return set_cookies(render(request, "secretario/manter_professor_em_turma.html", context), login)

def procurar_disciplina_em_curso(request: HttpRequest):
    """Página inicial para buscas de disciplina_em_curso"""
    context, login = check_login(request)
    if not isinstance(context, dict):
        return context
    
    filtro = request.GET.get("filtro", "")
    context["resultados"] = []
    if filtro.isnumeric():
        response, curso = conn.consultar.curso(login.token, int(filtro)) #disciplinas
        for n in range(0, len(curso.disciplinas)):
            curso.disciplinas[n].id_curso = curso.id
        context["resultados"] = curso.disciplinas
        
    # Adicionando o obj ao contexto e respondendo o request.
    return set_cookies(render(request, "secretario/manter_disciplina_em_curso.html", context), login)

def procurar_aluno_em_curso(request: HttpRequest):
    """Página inicial para buscas de curso_matriculado"""
    context, login = check_login(request)
    if not isinstance(context, dict):
        return context
    
    filtro = request.GET.get("filtro", "")
    response, curso_matriculado = conn.procurar.curso_matriculado(login.token, filtro)
    context["resultados"] = curso_matriculado
    
    # Adicionando o obj ao contexto e respondendo o request.
    return set_cookies(render(request, "secretario/manter_aluno_em_curso.html", context), login)

def editar_professor_em_turma(request: HttpRequest):
    context, login = check_login(request)
    if not isinstance(context, dict):
        return context
    
    id = request.GET.get("id", "")
    if id != "":
        response, dm = conn.consultar.disciplina_ministrada(login.token, id)
        context["cadastro"] = dm
    else:
        context["cadastro"] = None

    # Adicionando o obj ao contexto e respondendo o request.
    return set_cookies(render(request, "secretario/info_professor_em_turma.html", context), login)

def professor_em_turma_salvar(request: HttpRequest):
    context, login = check_login(request)
    if not isinstance(context, dict):
        return context

    id = request.GET.get("id", "")
    context["status"] = {"200_delete":False, "delete_error":False, "200":False, "400":False, "409":False, "500":False, "418": False}

    professor = conn.consultar.professor(login.token, request.GET.get("id_professor", ""))[1]
    turma = conn.consultar.turma(login.token, request.GET.get("id_turma", ""))[1]
    disciplina = conn.consultar.disciplina(login.token, request.GET.get("id_disciplina", ""))[1]

    encerrada = True if request.GET.get("encerrada", "") == "on" else False
    coordenador = True if request.GET.get("coordenador", "") == "on" else False

    obj = api.Disciplina_Ministrada(
        disciplina=disciplina,
        professor=professor,
        turma=turma,
        encerrada= encerrada,
        coordenador=coordenador
    )

    if professor == None or turma == None or disciplina == None:
        context["status"]["400"] = True
        return set_cookies(render(request, "secretario/info_professor_em_turma.html", context), login)
    elif id == "":
        response = conn.cadastrar.disciplina_ministrada(login.token, obj)
    else:
        response = conn.editar.disciplina_ministrada(login.token, id, obj)
 
    if response.status_code == 200:
        context["status"]["200"] = True
    if response.status_code == 400 and response.text != "Este professor já ministra esta disciplina nesta turma":
        context["status"]["400"] = True
    if response.status_code == 409 or response.text == "Este professor já ministra esta disciplina nesta turma":
        context["status"]["409"] = True
    if response.status_code == 500:
        context["status"]["500"] = True
    return set_cookies(render(request, "secretario/info_professor_em_turma.html", context), login)

def professor_em_turma_apagar(request: HttpRequest):
    context, login = check_login(request)
    if not isinstance(context, dict):
        return context

    id = request.GET.get("id", "")
    context["status"] = {"200_delete":False, "delete_error":False, "200":False, "400":False, "409":False, "500":False, "418": False}

    response = conn.apagar.disciplina_ministrada(login.token, id)

    if response.status_code == 200:
        context["status"]["200_delete"] = True
    elif response.status_code == 418:
        context["status"]["418"] = True
    else:
        context["status"]["delete_error"] = True
    return set_cookies(render(request, "secretario/info_professor_em_turma.html", context), login)

def editar_disciplina_em_curso(request: HttpRequest):
    context, login = check_login(request)
    if not isinstance(context, dict):
        return context
    
    context["cadastro"] = None
    # Adicionando o obj ao contexto e respondendo o request.
    return set_cookies(render(request, "secretario/info_disciplina_em_curso.html", context), login)

def disciplina_em_curso_salvar(request: HttpRequest):
    context, login = check_login(request)
    if not isinstance(context, dict):
        return context

    context["status"] = {"200_delete":False, "delete_error":False, "200":False, "400":False, "409":False, "500":False, "418": False}

    if not request.GET.get("id_disciplina", "").isnumeric() or not request.GET.get("id_curso", "").isnumeric():
        context["status"]["400"] = True
        return set_cookies(render(request, "secretario/info_disciplina_em_curso.html", context), login)
    
    response = conn.cadastrar.disciplina_em_curso(login.token, int(request.GET.get("id_curso", "")), int(request.GET.get("id_disciplina", "")))
 
    if response.status_code == 200:
        context["status"]["200"] = True
    if response.status_code == 400 and response.text:
        context["status"]["400"] = True
    if response.status_code == 409 or response.text:
        context["status"]["409"] = True
    if response.status_code == 500:
        context["status"]["500"] = True
    return set_cookies(render(request, "secretario/info_disciplina_em_curso.html", context), login)

def disciplina_em_curso_apagar(request: HttpRequest):
    context, login = check_login(request)
    if not isinstance(context, dict):
        return context

    context["status"] = {"200_delete":False, "delete_error":False, "200":False, "400":False, "409":False, "500":False, "418": False}
    response = conn.apagar.disciplina_em_curso(login.token, int(request.GET.get("id_curso", "")), int(request.GET.get("id_discilina", "")))
    if response.status_code == 200:
        context["status"]["200_delete"] = True
    elif response.status_code == 418:
        context["status"]["418"] = True
    else:
        context["status"]["delete_error"] = True
    return set_cookies(render(request, "secretario/manter_disciplina_em_curso.html", context), login)

def editar_aluno_em_curso(request: HttpRequest):
    context, login = check_login(request)
    if not isinstance(context, dict):
        return context
    
    id = request.GET.get("id", "")
    if id != "":
        response, dm = conn.consultar.curso_matriculado(login.token, id)
        context["cadastro"] = dm
    else:
        context["cadastro"] = None

    # Adicionando o obj ao contexto e respondendo o request.
    return set_cookies(render(request, "secretario/info_aluno_em_curso.html", context), login)

def aluno_em_curso_salvar(request: HttpRequest):
    context, login = check_login(request)
    if not isinstance(context, dict):
        return context

    id = request.GET.get("id", "")
    context["status"] = {"200_delete":False, "delete_error":False, "200":False, "400":False, "409":False, "500":False, "418": False}

    aluno = conn.consultar.aluno(login.token, request.GET.get("id_aluno", ""))[1]
    turma = conn.consultar.turma(login.token, request.GET.get("id_turma", ""))[1]
    curso = conn.consultar.curso(login.token, request.GET.get("id_curso", ""))[1]

    finalizado = True if request.GET.get("finalizado", "") == "on" else False
    trancado = True if request.GET.get("trancado", "") == "on" else False
    semestre_atual = int(request.GET.get("semestre_atual", "")) if request.GET.get("semestre_atual", "").isnumeric() else 1

    obj = api.Curso_Matriculado(
        curso=curso,
        aluno=aluno,
        turma=turma,
        semestre_atual=semestre_atual,
        trancado=trancado,
        finalizado=finalizado
    )

    if aluno == None or turma == None or curso == None:
        context["status"]["400"] = True
        return set_cookies(render(request, "secretario/info_aluno_em_curso.html", context), login)
    elif id == "":
        response = conn.cadastrar.curso_matriculado(login.token, obj)
    else:
        response = conn.editar.curso_matriculado(login.token, id, obj)
 
    print(f"status code: {response.status_code} {response.text}")
    if response.status_code == 200:
        context["status"]["200"] = True
    if (response.status_code == 400 or response.status_code == 404) and response.text != "Este aluno já faz parte desta turma":
        context["status"]["400"] = True
    if response.status_code == 409 or response.text == "Este aluno já faz parte desta turma":
        context["status"]["409"] = True
    if response.status_code == 500:
        context["status"]["500"] = True
    return set_cookies(render(request, "secretario/info_aluno_em_curso.html", context), login)

def aluno_em_curso_apagar(request: HttpRequest):
    context, login = check_login(request)
    if not isinstance(context, dict):
        return context

    id = request.GET.get("id", "")
    context["status"] = {"200_delete":False, "delete_error":False, "200":False, "400":False, "409":False, "500":False, "418": False}

    response = conn.apagar.curso_matriculado(login.token, id)

    if response.status_code == 200:
        context["status"]["200_delete"] = True
    elif response.status_code == 418:
        context["status"]["418"] = True
    else:
        context["status"]["delete_error"] = True
    return set_cookies(render(request, "secretario/info_aluno_em_curso.html", context), login)

def aluno_salvar(request: HttpRequest):
    context, login = check_login(request)
    if not isinstance(context, dict):
        return context

    id = request.GET.get("id", "")
    context["status"] = {"200_delete":False, "delete_error":False, "200":False, "400":False, "409":False, "500":False, "418": False}

    obj = api.Aluno(
        nome = request.GET.get("nome", ""),
        rg = int(request.GET.get("rg", "")),
        cpf = int(request.GET.get("cpf", "")),
        telefone = int(request.GET.get("telefone", "")),
        email = request.GET.get("email", "")
    )

    if id == "":
        response = conn.cadastrar.aluno(login.token, obj)
    else:
        response = conn.editar.aluno(login.token, id, obj)
 
    if response.status_code == 200:
        context["status"]["200"] = True
    if response.status_code == 400:
        context["status"]["400"] = True
    if response.status_code == 409:
        context["status"]["409"] = True
    if response.status_code == 500:
        context["status"]["500"] = True
    return set_cookies(render(request, "secretario/info_aluno.html", context), login)

def curso_salvar(request: HttpRequest):
    context, login = check_login(request)
    if not isinstance(context, dict):
        return context

    id = request.GET.get("id", "")
    context["status"] = {"200_delete":False, "delete_error":False, "200":False, "400":False, "409":False, "500":False, "418": False}

    obj = api.Curso(
        nome = request.GET.get("nome", ""),
        aulas_totais=int(request.GET.get("aulas_totais", "")),
        carga_horaria=int(request.GET.get("carga_horaria", ""))
    )

    if id == "":
        response = conn.cadastrar.curso(login.token, obj)
    else:
        response = conn.editar.curso(login.token, id, obj)
 
    if response.status_code == 200:
        context["status"]["200"] = True
    if response.status_code == 400:
        context["status"]["400"] = True
    if response.status_code == 409:
        context["status"]["409"] = True
    if response.status_code == 500:
        context["status"]["500"] = True
    return set_cookies(render(request, "secretario/info_curso.html", context), login)

def turma_salvar(request: HttpRequest):
    context, login = check_login(request)
    if not isinstance(context, dict):
        return context

    id = request.GET.get("id", "")
    context["status"] = {"200_delete":False, "delete_error":False, "200":False, "400":False, "409":False, "500":False, "418": False}

    
    curso = conn.consultar.curso(login.token, int(request.GET.get("id_curso", "")))[1]
    if curso == None:
        context["status"]["400"] = True
        return set_cookies(render(request, "secretario/info_turma.html", context), login)

    obj = api.Turma(
        nome=request.GET.get("nome", ""),
        curso=curso
    )

    if id == "":
        response = conn.cadastrar.turma(login.token, obj)
    else:
        response = conn.editar.turma(login.token, id, obj)
 
    if response.status_code == 200:
        context["status"]["200"] = True
    if response.status_code == 400:
        context["status"]["400"] = True
    if response.status_code == 409:
        context["status"]["409"] = True
    if response.status_code == 500:
        context["status"]["500"] = True
    return set_cookies(render(request, "secretario/info_turma.html", context), login)

def disciplina_salvar(request: HttpRequest):
    context, login = check_login(request)
    if not isinstance(context, dict):
        return context

    id = request.GET.get("id", "")
    context["status"] = {"200_delete":False, "delete_error":False, "200":False, "400":False, "409":False, "500":False, "418": False}

    obj = api.Disciplina(
        nome = request.GET.get("nome", "")
    )

    if id == "":
        response = conn.cadastrar.disciplina(login.token, obj)
    else:
        response = conn.editar.disciplina(login.token, id, obj)
 
    if response.status_code == 200:
        context["status"]["200"] = True
    if response.status_code == 400:
        context["status"]["400"] = True
    if response.status_code == 409:
        context["status"]["409"] = True
    if response.status_code == 500:
        context["status"]["500"] = True
    return set_cookies(render(request, "secretario/info_disciplina.html", context), login)

def __apagar(request: HttpRequest, funcao, path):
    context, login = check_login(request)
    if not isinstance(context, dict):
        return context

    id = request.GET.get("id", "")
    context["status"] = {"200_delete":False, "delete_error":False, "200":False, "400":False, "409":False, "500":False, "418": False}

    response = funcao(login.token, id)

    if response.status_code == 200:
        context["status"]["200_delete"] = True
    else:
        context["status"]["delete_error"] = True
    return set_cookies(render(request, path, context), login)

def aluno_apagar(request: HttpRequest):
    return __apagar(request, conn.apagar.aluno, "secretario/info_aluno.html")

def curso_apagar(request: HttpRequest):
    return __apagar(request, conn.apagar.curso, "secretario/info_curso.html")

def turma_apagar(request: HttpRequest):
    return __apagar(request, conn.apagar.turma, "secretario/info_turma.html")

def disciplina_apagar(request: HttpRequest):
    return __apagar(request, conn.apagar.disciplina, "secretario/info_disciplina.html")