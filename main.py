from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
from fastapi import FastAPI

app = FastAPI(title='Horoscope')

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

url = "https://dzen.ru/topic/horoscope"


znak_zodiak = {
    'овен': 'oven',
    'телец': 'telec', 
    'близнецы': 'bliznec',
    'рак': 'rak',
    'лев': 'lev',
    'дева': 'deva',
    'весы': 'vesy',
    'скорпион': 'skorpion',
    'стрелец': 'strelec',
    'козерог': 'kozerog',
    'водолей': 'vodoley',
    'рыбы': 'ryby'
}

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/horoscope", response_class=HTMLResponse)
async def horoscope(request: Request, zodiac_sign: str = Form(...)):
    pass