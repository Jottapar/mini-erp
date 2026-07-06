from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.core.config import settings
from app.db.session import init_db



@asynccontextmanager
async def lifespan(app:FastAPI):
    print(f'Iniciando aplicacion')
    init_db()
    yield
    print('Apagando')



app = FastAPI(
    title='MiniERP',
    version= settings.VERSION,
    lifespan=lifespan
)


@app.get('/')
def raiz():
    return {
        'mesnaje':'Bienvenido al MiniERP',
        'Version': settings.VERSION
    }