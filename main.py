from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "你好，这是我的API"}

@app.get("/hello/{name}")
def hello(name: str):
    return {"message": f"你好，{name}"}
