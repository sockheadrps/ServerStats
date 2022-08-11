from fastapi import (
    FastAPI,
    Request,
    HTTPException,
    WebSocket,
)
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from utilities.connection_manager import Manager
from utilities.stats import Computer
import logging
import typing
import uvicorn
import json

connected_services = {}

app = FastAPI()
connection_manager = Manager()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory=r"C:\Users\rpski\Desktop\Example Code\ServStats\static"), name="static")

logging.basicConfig(filename="./logs/logs.log", filemode="w", level=logging.DEBUG)


@app.get("/favicon.ico")
async def favicon() -> typing.NoReturn:
    # No current FavIcon - fix later
    raise HTTPException(status_code=403, detail="No favicon")


@app.get("/stats", response_class=HTMLResponse)
def stats_endpoint(request: Request) -> templates.TemplateResponse:
    """
    HTTP endpoint to serve the Server Statistics Dashboard
    :param request: HTTP Request from Client
    :return: Returns the associated HTML files to the requesting client
    """
    return templates.TemplateResponse(
        "index.html", {"request": request}
    )


@app.websocket("/ws/stats")
async def stats_websocket(client_websocket: WebSocket):
    """
    Web Socket endpoint for communicating the "Server Statistics" in JSON to the client. Communication with the
    data visualization client is done here.
    :param client_websocket: Incoming Web Socket request.
    :return: No explicit return, just continuous requests for information from client
    """

    # Create manager object based on 'sec-websocket-key' and track connected services
    global connected_services
    await connection_manager.connect(client_websocket)

    # Initial connection
    await client_websocket.send_json({"event": "CONNECT"})
    while True:
        # Client sending data....
        data = await client_websocket.receive()

        # Handling for websocket disconnect code
        if 'code' in data.keys():
            if data['code'] == 1006:
                disconnection_service = await connection_manager.disconnect_websocket(client_websocket)
                connected_services.pop(disconnection_service)
                break

        # otherwise, process data
        if 'text' in data.keys():
            data_dict = json.loads(data['text'])

            match data_dict["event"]:
                case "CONNECT":
                    # Flagging which services are active
                    if data_dict['client'] == "SERVER-STATS":
                        connected_services[client_websocket.headers['sec-websocket-key']] = "SERVER-STATS"
                    if data_dict['client'] == "TWITCH-BOT":
                        connected_services[client_websocket.headers['sec-websocket-key']] = "TWITCH-BOT"
                # Server-stats client requesting data
                case "data-request":
                    if "TWITCH-BOT" in connected_services:
                        await client_websocket.send_json(
                                {"event": "DATAREQUEST", "data": Computer.get_stats_dict(), "TWITCH": True})
                    else:
                        await client_websocket.send_json(
                            {"event": "DATAREQUEST", "data": Computer.get_stats_dict(), "TWITCH": False})


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
