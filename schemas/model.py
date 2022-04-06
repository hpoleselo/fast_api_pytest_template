from pydantic import BaseModel

class IncomingPayload(BaseModel):
    name: str
    age: int