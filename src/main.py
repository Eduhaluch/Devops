import random
from fastapi import FastAPI

app = FastAPI()
@app.get("/funcao_teste")
async def funcao_teste():
    return {"teste": True, "num_aleatorio": random.randint(0, 5000)}


@app.get("/")
async def root():
    return {"message": "Hello World"}
#alo

@app.get("/certo")
async def deucerto():
    return {"teste": "se viu é pq deu certo!"}