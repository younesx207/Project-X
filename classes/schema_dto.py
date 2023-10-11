from pydantic import BaseModel




# Model Pydantic = Datatype
class Event(BaseModel):
    id: str
    title: str
    
class EventNoID(BaseModel):
    title: str