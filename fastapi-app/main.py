from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def read_root():
    return "Hola FastApi"

@app.get("/Pagina")
def Pagina():
    return {"url": "https://jansonAndres.com"}