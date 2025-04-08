from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.core.websocket import connection_manager

router = APIRouter()

@router.websocket("/simulation")
async def websocket_endpoint(websocket: WebSocket):
    await connection_manager.connect(websocket)
    try:
        while True:
            # Keep connection alive (optionally process incoming messages)
            await websocket.receive_text()
    except WebSocketDisconnect:
        connection_manager.disconnect(websocket)
