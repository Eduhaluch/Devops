from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
#alo

@app.get("/certo")
async def deucerto():
    return {"teste": "se viu é pq deu certo!"}