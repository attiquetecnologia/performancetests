from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def index():
    return {"Hello": "World"}


@app.get("/api")
async def api():
    return [
        {'id': 1, 'name': 'Ronald'},
        {'id': 2, 'name': 'Ronald'},
        {'id': 3, 'name': 'Ronald'},
        {'id': 4, 'name': 'Ronald'},
        {'id': 5, 'name': 'Ronald'},
        {'id': 6, 'name': 'Ronald'},
        {'id': 7, 'name': 'Ronald'},
        {'id': 8, 'name': 'Ronald'},
        {'id': 9, 'name': 'Ronald'},
        {'id': 10, 'name': 'Ronald'},
    ]