import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os
from pathlib import Path

app = FastAPI(title="Ranjith AI Engineer Portfolio.")


BASE_DIR = Path(__file__).resolve().parent

app.mount(
    "/static",
    StaticFiles(directory=BASE_DIR / "static"),
    name="static"
)

templates = Jinja2Templates(directory=BASE_DIR / "templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Landing page"""
    return templates.TemplateResponse("index.html", {"request": request, "title": "Home"})


@app.get("/projects", response_class=HTMLResponse)
async def projects(request: Request):
    """Projects page"""
    return templates.TemplateResponse("projects.html", {"request": request, "title": "Projects"})


@app.get("/chatbot", response_class=HTMLResponse)
async def chatbot_page(request: Request):
    """Chatbot demo page"""
    return templates.TemplateResponse("chatbot.html", {"request": request, "title": "Chatbot"})


@app.get("/resume", response_class=HTMLResponse)
async def resume_page(request: Request):
    """Resume page (download button will be wired later)"""
    return templates.TemplateResponse("resume.html", {"request": request, "title": "Resume"})


if __name__ == "__main__":

    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, port=port)