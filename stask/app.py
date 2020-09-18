import os

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import logic


app = FastAPI(title="Sasha")
app.mount('/static',
        StaticFiles(directory=os.path.join(os.getcwd(), 'static')),
        name='static')

templates = Jinja2Templates(directory=os.path.join(os.getcwd(), 'templates'))


@app.get('/')
def index(request: Request):
    table = logic.Table(use_config_file=True)
    table.defect()
    table.run()
    return templates.TemplateResponse('index.html', {
        'request': request,
        'table': table.table,
    })

