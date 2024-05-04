from pydantic import BaseModel, ConfigDict
from fastapi import Request , Form
from typing import Optional, Union
class R(BaseModel):
    username: str 
    password: str 
    
class Registration_form:
    def __init__(self,re: Request):
        self.request = re
        self.username: str = None
        self.password: str = None
    async def load_data(self):
        form = await self.request.form()
        self.username = form.get("a")
        self.password = form.get("b")