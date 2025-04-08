
from fastapi import FastAPI
from app.api import auth, users, simulation, lessons, levels, websocket_endpoint

app = FastAPI()

app.include_router(auth.router, prefix="/api/auth")
app.include_router(users.router, prefix="/api/users")
app.include_router(simulation.router, prefix="/api/simulation")
app.include_router(lessons.router, prefix="/api/lessons")
app.include_router(levels.router, prefix="/api/levels")
app.include_router(websocket_endpoint.router, prefix="/ws")

@app.get("/")
def read_root():
    return {"message": "Stock Market Learning Platform Prototype"}
