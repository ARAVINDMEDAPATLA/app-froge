from fastapi import FastAPI

app = FastAPI(title="App Forge API")

@app.get("/")
def read_root():
    return {"message": "Welcome to the App Forge API"}
