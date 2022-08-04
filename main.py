from fastapi import (
    FastAPI,
    Request,
    HTTPException,
    WebSocket,
    WebSocketDisconnect,
)
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from ConnectionManager import Manager
from stats import Computer
import logging
import typing
import uvicorn
import uuid


app = FastAPI()
connection_manager = Manager()
templates = Jinja2Templates(directory="templates")
app.mount('/static', StaticFiles(directory='static'), name='static')

logging.basicConfig(filename='logs.log', filemode='w', level=logging.DEBUG)


def generate_id() -> str:
    """
    Generates a UUID string for unique client IDs
    :return: String representation of UUID object
    """
    return str(uuid.uuid4())


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
    client_id = generate_id()
    return templates.TemplateResponse(
        "index.html", {"request": request, "id": client_id}
    )


@app.websocket("/ws/stats")
async def stats_websocket(client_websocket: WebSocket):
    """
    Web Socket endpoint for communicating the "Server Statistics" in JSON to the client. Communication with the
    client is done here.
    :param client_websocket: Incoming Web Socket request
    :return: No explicit return, just continous requests for information from client
    """
    await connection_manager.connect(client_websocket)
    try:
        # Initial connection
        await client_websocket.send_json({"event": "CONNECT"})
        while True:
            try:
                # Client sending data....
                data = await client_websocket.receive_json()
                # DATAREQUEST is the asking protocol from the client, requesting the Hardware stats
                if data['event'] == 'DATAREQUEST':
                    await client_websocket.send_json({
                        "event": "DATAREQUEST", 
                        "data": Computer.get_stats_dict()
                    })
                else:
                    # Log, if for some reason we get some other type of protocol from the client
                    logging.debug(data)
            except WebSocketDisconnect:
                await connection_manager.disconnect_websocket(client_websocket)
            except Exception as e:
                logging.debug(e)
    except Exception as e:
        logging.debug(e)

if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
