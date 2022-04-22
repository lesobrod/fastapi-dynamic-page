
from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse

app = FastAPI(title="List API")

with open('template.html', 'r', encoding='UTF-8') as file:
    HTML = file.read()

@app.get("/")
async def get():
    return HTMLResponse(HTML)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(data)