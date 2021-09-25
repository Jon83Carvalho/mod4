from fastapi import FastAPI

app=FastAPI()

@app.get("/api")
async def root():
    return {'message':'Legal, funcionou'}

@app.get("/api/{name}")
async def get_user(name):
    return {
        "name":name,
        "Message":f"Hello, {name} fastAPI", 
    }