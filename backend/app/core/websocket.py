from typing import List
import asyncio
from fastapi import WebSocket

# --- Observer Pattern for Real-Time Updates ---

class Observer:
    def update(self, data):
        raise NotImplementedError("Subclasses must implement update method.")

class SimulationNotifier:
    def __init__(self):
        self._observers: List[Observer] = []

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self, data):
        for observer in self._observers:
            observer.update(data)

# --- WebSocket Observer Implementation ---
class WebSocketObserver(Observer):
    def __init__(self, websocket: WebSocket):
        self.websocket = websocket

    def update(self, data):
        # Schedule an asynchronous send
        asyncio.create_task(self.websocket.send_json(data))

# --- Connection Manager for WebSockets ---
class ConnectionManager:
    def __init__(self):
        self.active_observers: List[WebSocketObserver] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        observer = WebSocketObserver(websocket)
        self.active_observers.append(observer)
        simulation_notifier.attach(observer)

    def disconnect(self, websocket: WebSocket):
        observer = next((obs for obs in self.active_observers if obs.websocket == websocket), None)
        if observer:
            self.active_observers.remove(observer)
            simulation_notifier.detach(observer)

# Global instances
simulation_notifier = SimulationNotifier()
connection_manager = ConnectionManager()
