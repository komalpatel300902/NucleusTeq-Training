from pydantic import BaseModel

class Register(BaseModel):
    emp_id : str
    name : str 
    email : str
    mobile : str
    department : str