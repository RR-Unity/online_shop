import uvicorn

from app.api.server import create_api_server
from app.core.config import Config
from app.core.containers import wire_modules

app = create_api_server()
wire_modules()

if __name__ == '__main__':
    config = Config.load_config()
    uvicorn.run(
        'main:app',
        host=config.uvicorn_host,
        port=config.uvicorn_port,
        reload=config.developer_mode,
        workers=config.uvicorn_workers,
    )
