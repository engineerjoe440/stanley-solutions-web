################################################################################
"""
Stanley Soutions Web
*Engineering and Creativity - All Under One Hat*

(c) 2021 - Joe Stanley
"""
################################################################################

# Imports
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


# Stand Up the App
app = FastAPI()

# Mount Static Files
app.mount("/static", StaticFiles(directory="static"), name="static")
TEMPLATES = Jinja2Templates(directory="templates")

# Index Page
@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return await get_404(request)

@app.get("/404", response_class=HTMLResponse)
async def get_404(request: Request):
    return TEMPLATES.TemplateResponse(
        "dog.html",
        {
            "request": request,
            "CODE": "404",
        },
        status_code=404,
    )

@app.get("/503", response_class=HTMLResponse)
async def get_503(request: Request):
    return TEMPLATES.TemplateResponse(
        "skull.html",
        {
            "request": request,
            "CODE": "503",
        },
        status_code=503,
    )

@app.get("/418", response_class=HTMLResponse)
async def get_418(request: Request):
    return TEMPLATES.TemplateResponse(
        "coffee.html",
        {
            "request": request,
            "CODE": "418",
        },
        status_code=418,
    )

# Custom Page
@app.get("/err/{error_code}", response_class=HTMLResponse)
async def error_page(request: Request, error_code: str):
    if not (error_code.isdigit() and len(error_code) == 3):
        await root()
    return TEMPLATES.TemplateResponse(
        "skull.html",
        {
            "request": request,
            "CODE": error_code,
        },
        status_code=int(error_code),
    )



@app.get("/favicon.ico")
async def main():
    return FileResponse("./static/favicon.svg")