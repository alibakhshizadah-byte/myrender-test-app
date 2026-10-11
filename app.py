from fastapi import FastAPI

app = FastAPI(title="MyRender Test App")

@app.get("/")
def home():
    return {
        "status": "ok",
        "message": "MyRender deployment works!"
    }

@app.get("/health")
def health():
    return {"status": "healthy"}
