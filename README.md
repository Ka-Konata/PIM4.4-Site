# PIM4.4 Site
Um site para o PIM com integração na nossa API.
> versão do python: 3.9.10

## Clonando o Repositório
1. Fale comigo para pegar informações sobre as variáveis de ambiente.
2. Em "mysite/" crie um arquivo .env com todas as variáveis de ambiente.
3. Caso você esteja no windows, abra um terminal como administrador e use "Set-ExecutionPolicy Unrestricted -Force".
4. Crie um ambiente virtual com "python -m venv pim4site"
5. Ative o ambiente virtual com o comando ".\pim4site\Scripts\activate".
6. Instale todas as bibliotecas com o comando "pip install -r requeriments.txt"
7. Vá para a pasta do servidor com "cd mysite".
8. Para iniciar o servidor, use o seguinte comando "python manage.py runserver".

## API Integration
Rotas que faltam integrar:
- [ ] /api/Curso/disciplina
- [ ] /api/Curso/disciplina
- [ ] /api/DisciplinaCursada/media/{id}
- [ ] /api/DisciplinaCursada/frequencia/{id}
- [ ] /api/DisciplinaCursada/situacao{id}
- [ ] /api/File/conteudo/{file}
- [ ] /api/File/boletim/{id}
- [ ] /api/File/historico/{id}
- [ ] /api/File/declaracao/{id}
- [ ] /api/File/relatorio/{id}