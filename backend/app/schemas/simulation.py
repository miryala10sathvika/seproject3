from pydantic import BaseModel

class SimulationRequest(BaseModel):
    scenario_type: str

class SimulationResponse(BaseModel):
    result: str
