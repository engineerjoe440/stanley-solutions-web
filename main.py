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


# Define the Generic Page
GENERIC_HTML = """<!DOCTYPE html>
<html>
<head>
<link href='https://fonts.googleapis.com/css?family=Aldrich' rel='stylesheet'>
<link href='https://fonts.googleapis.com/css?family=Amatic SC' rel='stylesheet'>
<style>
.parent {
    position: absolute;
    top: 10%;
    left: 5%
}

.child {
    position: absolute;
    bottom: -100%;
    right: -50%;
}

body {
    background-image: url('./static/dogxray.jpg');
    background-repeat: no-repeat;
    background-attachment: fixed;
    background-position: right;
    background-color: black;
}

footer {
    position: absolute;
    bottom: 0;
    color: #81BCB8;
    font-family: 'Amatic SC';
    font-size: 16px;
}

h1 {
    text-transform: uppercase;
    color: #0D5D5A;
    font-family: 'Aldrich';
    font-size: 40px;
    text-align: right;
}

p {
    color: #81BCB8;
    font-family: 'Amatic SC';
    font-size: 32px;
}
</style>
</head>
<body>

<div class="parent">
<h1>Math Homework isn't<br>all the dog ate.</h1>

<div class="child">
<p>Somehow it also got its jaws around our HTML, too.<br>Maybe next time we won't
just write it out on graph paper...</p>
</div>
</div>

<footer>
© 2021 - Stanley Solutions
</footer>

</body>
</html>"""


# Stand Up the App
app = FastAPI()

# Mount Static Files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Index Page
@app.get("/")
async def root():
    return HTMLResponse(content=GENERIC_HTML, status_code=503)



@app.get("/favicon.ico")
async def main():
    return FileResponse("./static/favicon.svg")