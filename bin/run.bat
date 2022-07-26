start powershell /C ./server.bat

cd ../
poetry install
poetry run py -m aiohttp.web -H localhost -P 3000 backend.main:init_app
