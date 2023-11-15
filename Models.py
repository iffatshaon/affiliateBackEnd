from pydantic import BaseModel

class Register(BaseModel):
    firstName: str
    lastName: str
    userName: str
    email: str
    password: str