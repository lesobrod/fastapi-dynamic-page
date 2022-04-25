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
    counter = 0
    await websocket.accept()
    while True:
        # receive data
        recv_data = await websocket.receive_text()
        counter += 1
        # send data
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        new_message = {
            'id': counter,
            'timestamp': dt_string,
            'text': recv_data
        }
        await websocket.send_json(new_message)
