from pydantic import BaseModel

class Todo(BaseModel):
    name:str
    mobile:int
    email:str
class Find(BaseModel):
    name:str