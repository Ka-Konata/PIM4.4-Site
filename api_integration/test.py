import api, json
from models.analistarh import AnalistaRH
from ast import literal_eval

conn = api.Connection("https://pim44-api.victorgrferreir.repl.co/api")
u = AnalistaRH(nome="Admin", cpf=12345, rg=12345, telefone=12345, email="12345@gmail.com")
id = 10001
senha = "KLAd9d9bqwyu"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6ImF0K2p3dCJ9.eyJlbWFpbCI6IjEyMzQ1QGdtYWlsLmNvbSIsInJvbGUiOiJBbmFsaXN0YVJIIiwiaWQiOiIxMDAwMSIsImp0aSI6IjVhNzQwZjNjLWJjOWItNGM3Zi05ZDhlLTFmZDczZDFhY2MyMSIsIm5iZiI6MTY5NjEyNjg4OCwiZXhwIjoxNjk2MTMwNDg4LCJpYXQiOjE2OTYxMjY4ODgsImlzcyI6ImxvY2FsaG9zdDo3MjQ2IiwiYXVkIjoiaHR0cHM6Ly9sb2NhbGhvc3Q6NzI0NiJ9.8iAyGJ85YH4GQ4--Zq4lXWKwq0QyGb2kdH_Xc7NA9QM"
refresh_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6InJ0K2p3dCJ9.eyJpZCI6IjEwMDAxIiwianRpIjoiZmYyM2NhNmQtY2VjYy00MTRiLTk0N2UtOWZiZDRhZTA2OTM4IiwibmJmIjoxNjk2MTI2ODg4LCJleHAiOjE2OTY3MzE2ODgsImlhdCI6MTY5NjEyNjg4OCwiaXNzIjoibG9jYWxob3N0OjcyNDYiLCJhdWQiOiJodHRwczovL2xvY2FsaG9zdDo3MjQ2In0.-o7tA8-v2rktff8PHM0l0IQmnnufWB02btCrPihYluQ"

#r = conn.refresh(10001, token, refresh_token)
r = conn.refresh(id, token, refresh_token)
if r.ok:
    print("Type: ", r.headers["Content-Type"])
    print("Text: ", str(r.text))
    print("JSON: ", r.json())
    print("Content", r.content)
else:
    r.raise_for_status()
#print(r.status_code, r._content)