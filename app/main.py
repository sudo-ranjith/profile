from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
import os

# Base directory of this file (works in Docker and locally)
BASE_DIR = Path(__file__).resolve().parent

# Initialize app
app = FastAPI(title="Ranjith Portfolio")

# Mount static directory
app.mount(
    "/static",
    StaticFiles(directory=BASE_DIR / "static"),
    name="static"
)

# Load templates directory
templates = Jinja2Templates(directory=BASE_DIR / "templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Landing page"""
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "title": "Home"}
    )


@app.get("/projects", response_class=HTMLResponse)
async def projects(request: Request):
    """Projects page"""
    return templates.TemplateResponse(
        "projects.html",
        {"request": request, "title": "Projects"}
    )


@app.get("/chatbot", response_class=HTMLResponse)
async def chatbot_page(request: Request):
    """Chatbot demo page"""
    return templates.TemplateResponse(
        "chatbot.html",
        {"request": request, "title": "Chatbot"}
    )


@app.get("/resume", response_class=HTMLResponse)
async def resume_page(request: Request):
    """Resume page (download button can link to PDF later)"""
    return templates.TemplateResponse(
        "resume.html",
        {"request": request, "title": "Resume"}
    )


# --- Entry point ---
if __name__ == "__main__":
    import uvicorn

    # Hugging Face Spaces requires port 7860
    port = int(os.environ.get("PORT", 7860))
    uvicorn.run(app, host="0.0.0.0", port=port)
