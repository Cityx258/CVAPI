import cv2
import numpy as np
from fastapi import FastAPI, WebSocket, WebSocketDisconnect

from detector import detect

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World!"}


@app.websocket("/ws")
async def track(ws: WebSocket):
    await ws.accept()
    try:
        while True:
            data = await ws.receive_bytes()
            await ws.send_json(offset(data))
    except WebSocketDisconnect:
        pass


def offset(data):
    frame = cv2.imdecode(np.frombuffer(data, np.uint8), cv2.IMREAD_COLOR)
    target = detect(frame) if frame is not None else None
    if target is None:
        return {"found": False}

    h, w = frame.shape[:2]
    return {
        "found": True,
        "dx": (target[0] - w / 2) / (w / 2),
        "dy": (target[1] - h / 2) / (h / 2),
    }
