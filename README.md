
# ServerStats
![Alt Text](https://github.com/sockheadrps/ServerStats/blob/main/55a89ef63e8b9f8c0350aec7eab0b20b.gif)
## _Server health at a glance!_

This is just a personal project utilizing some skills in a way that is meaningful to me. At the core, this project leverages serving a web client front end with FastAPI to monitor the health of my development server at home. Some notable skills:

- FastAPI Backend
- Websocket Communication
- ChartJS
- Pytest

## Features

A web front end to easily view CPU usage, RAM usage and Disk space graphically.
Three smaller, more detailed sections to view more in depth statistics on hardware


## Tech



- [FastAPI](https://fastapi.tiangolo.com/) -
- HTML/CSS/JS
- [ChartJS](https://www.chartjs.org/)
- [Poetry](https://python-poetry.org/docs/basic-usage/)
- [Pytest](https://docs.pytest.org/en/7.1.x/)

## Usage
- Run main.py on the computer you wish to monitor, then connect to it via LAN (http://LANIP:8080/stats)



## Installation

[Python 3.7+](https://www.python.org/)
    
To run:
```
poetry install
poetry run python main.py
```
Connect to your ip, at the endpoint '/stats' on port 8080
```
http://YOUR_IP:8080/stats (if accessing from a different client machine than the host)
http://localhost:8080/stats (if youre accessing from the host machine)
```
To run tests (development only):
```
poetry run pytest
```
## Development

Want to contribute? Great!


## License

MIT

**Free Software, Hell Yeah!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)




