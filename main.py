################################################################################
"""
Stanley Soutions Web
*Engineering and Creativity - All Under One Hat*

(c) 2021 - Joe Stanley
"""
################################################################################

# Imports
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


# Define the Generic Page
GENERIC_HTML = """"""


# Stand Up the App
app = FastAPI()

# Mount Static Files
app.mount("/static", StaticFiles(directory="static"), name="static")
TEMPLATES = Jinja2Templates(directory="templates")

# Index Page
@app.get("/")
async def root():
    return HTMLResponse(
        content=TEMPLATES.TemplateResponse(
            "dog.html",
            {
                "CODE": "503",
            },
        ),
        status_code=503,
    )

# Custom Page
@app.get("/err/{error_code}")
async def error_page(error_code: str):
    if not (error_code.isdigit() and len(error_code) == 3):
        await root()
    return HTMLResponse(
        content=TEMPLATES.TemplateResponse(
            "dog.html",
            {
                "CODE": error_code,
            },
        ),
        status_code=int(error_code),
    )



@app.get("/favicon.ico")
async def main():
    return FileResponse("./static/favicon.svg")