# REVIEW: imports should be sorted in groups: top is python standard library, middle is third party, bottom is local
import logging
import uuid

import uvicorn
from fastapi import FastAPI, HTTPException, Request, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# REVIEW: all internal imports should be relative
from .connection_manager import ConnectionManager
from .constants import STATIC_DIR
from .stats import Computer

# REVIEW: best practice for logger is to initialize logger settings in __ini__.py
# then get the logger when being used in a script. __name__ is going to return main which was
# the name of the logger
logger = logging.getLogger(__name__)

# REVIEW: the __main__.py (called a dunder main) is the top-level script that is executed when the program is run
# https://docs.python.org/3.8/library/__main__.html

# REVIEW: good to have a separate function for main and
# call it in the if statement below
app = FastAPI()
connection_manager = ConnectionManager()
templates = Jinja2Templates(directory="templates")
app.mount(
    "/static",
    # REVIEW: file paths should be constants in most cases
    StaticFiles(directory=STATIC_DIR),
    name="static",
)


def generate_id() -> str:
    """
    Generates a UUID string for unique client IDs
    :return: String representation of UUID object
    """
    return str(uuid.uuid4())


# REVIEW: not really needed to type NoRetur, can just have no type hint
# or type hint None if you really feel like it
@app.get("/favicon.ico")
async def favicon() -> None:
    # No current FavIcon - fix later
    raise HTTPException(status_code=403, detail="No favicon")


@app.get("/stats", response_class=HTMLResponse)
def stats_endpoint(request: Request) -> HTMLResponse:
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
    data visualization client is done here.
    :param client_websocket: Incoming Web Socket request.
    :return: No explicit return, just continuous requests for information from client
    """
    await connection_manager.connect(client_websocket)
    try:
        # Initial connection
        await client_websocket.send_json({"event": "CONNECT"})
        while True:
            try:
                # Client sending data....
                data = await client_websocket.receive_json()
                # DATAREQUEST is the asking protocol from the client requesting for the Hardware stats
                if data["event"] == "DATAREQUEST":
                    await client_websocket.send_json(
                        {"event": "DATAREQUEST", "data": Computer.get_stats_dict()}
                    )
                else:
                    # Log if for some reason we get unexpected communication protocol from the client
                    # REVIEW: want to log to a specific logger rather than all loggers
                    logger.debug(data)
            except WebSocketDisconnect:
                await connection_manager.disconnect_websocket(client_websocket)
                break
            except Exception as e:
                logger.debug(e)
    except Exception as e:
        logger.debug(e)


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
