from fastapi import APIRouter, HTTPException
from app.services.simulation_service import run_simulation

router = APIRouter()

@router.post("/{scenario_type}")
def simulate_market(scenario_type: str):
    """
    Starts a simulation based on the provided scenario type.
    Uses the Factory pattern to create a scenario and the Observer pattern
    to notify subscribers of simulation updates.
    """
    try:
        result = run_simulation(scenario_type)
        return {"result": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
