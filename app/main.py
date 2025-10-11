from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

app = FastAPI(title="Ranjith Portfolio")

# Static files (CSS, JS, images)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Templates folder
templates = Jinja2Templates(directory="app/templates")


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
    import uvicorn

    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, port=port)