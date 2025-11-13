from fastapi import FastAPI
from routes.products import products_router
from routes.users import user_router
from dotenv import load_dotenv
app = FastAPI()
load_dotenv()

app.include_router(products_router)
app.include_router(user_router)

@app.get("/")
def rota_inicial():
    return { 
        "message": "Olá mundo" 
    }
    
@app.get("/teste")
def rota_teste():
    return {
        "message": "Tá funcionando"
    }

