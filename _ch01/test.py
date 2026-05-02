from fastapi import FastAPI

app = FastAPI()

@app.get("/swarna")
def home():
    return {"hello" : "world"}