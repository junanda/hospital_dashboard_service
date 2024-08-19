from pydantic import BaseModel
from datetime import datetime as tim

class User(BaseModel):
    traceId: str
    username: str
    password: str
    role: str
    created_at: tim
    updated_at: tim

    class config:
        from_attributes = True


class RequestLogin(BaseModel):
    username: str
    password: str

    class config:
        from_attributes = True

