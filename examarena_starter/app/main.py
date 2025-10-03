from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Exam Arena MVP1")

# Serve static files (index.html) at root
app.mount("/", StaticFiles(directory="app/static", html=True), name="static")
