
# ServerStats
![Alt Text](https://github.com/sockheadrps/ServerStats/blob/main/88c629a5893c04a876ff51f0a740dcf1.gif)
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

## Installation

[Python 3.7+](https://www.python.org/)
    
To run:
```
poetry install
poetry run python -m server_stats
```
Connect to your ip, at the main endpoint on port 8000 (by default)
```
http://YOUR_IP:8000/(if accessing from a different client machine than the host)
http://localhost:8080/ (if youre accessing from the host machine)
```
To run tests (development only):
```
poetry run pytest
```
## Development

### Contributors

...

### TODO

- [ ] Temperature monitoring for Windows
- [ ] Visual display of temperature
- [ ] Js module for charts
- [ ] App integration tests strategy


## License

MIT

**Free Software, Hell Yeah!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)




