# Dreamy Dragons

This repository contains Dreamy Dragons team project for Python Discord Code Jam 2022.

## Development

### How to run using docker-compose:

#### Linux:
```bash
cd bin
./devstack up
```

### Windows:
```bat
cd bin
./devstack.bat up
```

Then open http://localhost:8080 in browser.

### How to run without docker


```bash
# first terminal
cd frontend
python3 -m http.server
# second terminal
poetry install
poetry shell # to activate virtualenv
python -m aiohttp.web -H localhost -P 3000 backend.main:init_app
```

Then open http://localhost:8000 in browser.
