from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from datetime import datetime

app = FastAPI(title="List API")

# Import html
with open('template.html', 'r', encoding='UTF-8') as file:
    HTML = file.read()


@app.get("/")
async def get() -> HTMLResponse:
    return HTMLResponse(HTML)


@app.websocket_route("/ws")
async def websocket_endpoint(websocket: WebSocket) -> None:
    await websocket.accept()
    while True:
        # receive data
        recv_data = await websocket.receive_text()

        # send data
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M")
        send_data = {
            'datetime': dt_string,
            'text': recv_data
        }
        await websocket.send_json(send_data)
