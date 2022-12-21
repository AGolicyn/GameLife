import asyncio
import json
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from websockets.exceptions import ConnectionClosedOK
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger
from .schemas import GameOptions
from .calculation import World

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=["*"],
)


@app.get('/')
def get_main():
    return 'Some msg'


async def sender(game: World, websocket: WebSocket):
    try:
        while not game.interrupt:
            alive_molecules = await game.live_an_epoch()
            alive_molecules = json.dumps(alive_molecules)
            await websocket.send_json(alive_molecules)
    except (WebSocketDisconnect, ConnectionClosedOK) as ex:
        logger.debug(ex)
        raise asyncio.CancelledError


async def receiver(game: World, websocket: WebSocket):
    try:
        while not game.interrupt:
            data = await websocket.receive_json()
            new_options = GameOptions(**data)
            game.refresh(new_options)
    except (WebSocketDisconnect, ConnectionClosedOK) as ex:
        logger.debug(ex)
        raise asyncio.CancelledError


@app.websocket('/ws')
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    logger.debug(f'Accepted websocket connection Client: {websocket.client}, Server: {websocket.url}')
    try:
        while True:
            init_data = await websocket.receive_json()
            options = GameOptions(**init_data)
            game = World(options)

            async with asyncio.TaskGroup() as tg:
                tg.create_task(sender(game, websocket))
                tg.create_task(receiver(game, websocket))
            break
    except WebSocketDisconnect as ex:
        print(f'Connection closed with {ex}')
    except Exception as e:
        logger.error(e)
