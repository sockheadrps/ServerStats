
# ServerStats
![Alt Text](https://github.com/sockheadrps/ServerStats/blob/main/18d3fabd7697a28ce7a5161f424964e5.gif)
## _Server health at a glance!_

This is just a personal project utilizing some skills in a way that is meaningful to me. At the core, this project leverages serving a web client front end with FastAPI to monitor the health of my development server at home. Some notable skills:

- FastAPI Backend
- Websocket Communication
- ChartJS

## Features

A web front end to easily view CPU usage, RAM usage and Disk space graphically.
Three smaller, more detailed sections to view more in depth statistics on hardware


## Tech



- [FastAPI](https://fastapi.tiangolo.com/) -
- HTML/CSS/JS
- [ChartJS](https://www.chartjs.org/)

## Usage
- Run main.py on the computer you wish to monitor, then connect to it via LAN (http://LANIP:8080/stats)



## Installation

[Python 3.7+](https://www.python.org/)
Install the required dependencies via the requirements.txt file
open the directory in your terminal and run main.py
    
To run:
```
poetry install
python run python main.py
```
Connect to your ip, at the endpoint '/stats' on port 8080
```
http://YOUR_IP:8080/stats (if accessing from a different client machine than the host)
http://localhost:8080/stats (if youre accessing from the host machine)
```
To run tests (development only):
```
poetry run pytets
```
## Development

Want to contribute? Great!


## License

MIT

**Free Software, Hell Yeah!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)




