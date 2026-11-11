#schema.py
## pydantic is a Python library used for data validation.
## BaseModel is the parent class provided by Pydantic.
from pydantic import BaseModel, ConfigDict

class TodoBase(BaseModel): 
    title: str
    description: str | None = None
    isCompleted: bool = False
    
class TodoCreate(TodoBase):
    pass

class Todo(TodoBase):
    id: int
## Pydantic needs to read the attributes of this object and convert them into a response matching your schema.
    model_config = ConfigDict(from_attributes=True)