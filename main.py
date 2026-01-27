from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
from fastapi import FastAPI

import horoscope

app = FastAPI(title='Horoscope')

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# @app.post("/horoscope", response_class=HTMLResponse)
# async def horoscope(request: Request, zodiac_sign: str = Form(...)):
#     pass

@app.get("/horoscope", response_class=HTMLResponse)
async def horos(request: Request):
     return templates.TemplateResponse("index.html", {"request": request})


@app.post("/horoscope", response_class=HTMLResponse)
async def post_horoscope(request: Request, sign: str = Form(...)):
     horoscope.znak = sign
     horo_text = f"Выбран знак: {horoscope.znak}"
    #  horoscope.get_horo(sign)
     hr_txt = horoscope.get_horo(sign)


     return templates.TemplateResponse('horoscope.html', {
          "request": request,
          "user_sign": sign,
          "horoscope": horo_text,
          "text": hr_txt
     })


if __name__ == "__main__":
     uvicorn.run(app, host="127.0.0.1", port=1488)