from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse


BASE_DIR = Path(__file__).resolve().parent.parent
FRONTEND_DIR = BASE_DIR / "frontend"

app = FastAPI(title="PyGravity Phase 1")


@app.get("/")
def index():
    return FileResponse(FRONTEND_DIR / "index.html")


@app.get("/api/status")
def status():
    return {"status": "ok", "phase": 1, "project": "PyGravity"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("backend.main:app", host="127.0.0.1", port=8000, reload=True)
