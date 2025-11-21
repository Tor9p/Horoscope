from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
from fastapi import FastAPI

from horoscope import get_horo

app = FastAPI(title='Horoscope')

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


get_horo()

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/horoscope", response_class=HTMLResponse)
async def horoscope(request: Request, zodiac_sign: str = Form(...)):
    pass


if __name__ == "__main__":
     uvicorn.run(app, host="127.0.0.1", port=8080)