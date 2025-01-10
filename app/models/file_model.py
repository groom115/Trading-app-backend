from pydantic import BaseModel, Field

class File(BaseModel):
    user: str
    broker: str
    api_key: str
    api_secret: str
    pnl: float
    margin: float
    max_risk: float

    class Config:
        
        allow_population_by_field_name = True

