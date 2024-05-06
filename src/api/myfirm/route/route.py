from fastapi import (APIRouter ,Form, Request)
from config.databases import sql , cursor
from model.models import Register
from schema.schema import list_serial
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

router = APIRouter()
templates = Jinja2Templates(directory = "templates")

@router.get("/register",response_class=HTMLResponse)
async def get_enter_employee_details(request: Request):
    return templates.TemplateResponse("register.html",{"request":request})

@router.post("/register",response_class=HTMLResponse)
async def enter_employee_details(request: Request, emp_id: str = Form(...),name:str = Form(...),email:str = Form(...),mobile:str = Form(...),department:str = Form(...)):
    info = Register(emp_id=emp_id, name=name,mobile=mobile,email=email,department=department)
    sql_query = f"INSERT INTO employees VALUES ('{info.emp_id}','{info.name}','{info.email}','{info.mobile}','{info.department}');"
    try:
        cursor.execute(sql_query)
    except Exception as e:
        print(e)
    else:
        sql.commit()
        print("Record added successfully !!!")
    return templates.TemplateResponse("register.html",{"request":request})


@router.get("/my_info",response_class=HTMLResponse)
async def my_info(request: Request):
    result = []
    sql_query = "SELECT * FROM employees;"
    try:
        cursor.execute(sql_query)
    except Exception as e:
        print(e.__context__)
    else:
        values = cursor.fetchall()
        result = list_serial(values)

    return templates.TemplateResponse("my_info.html",{"request": request,"employees":result})

 
@router.get("/update",response_class=HTMLResponse)
async def update(request : Request):
    return templates.TemplateResponse("update_name.html",{"request":request})

@router.put("/update/{emp_id}",response_class = HTMLResponse)
async def update_name(request: Request, emp_id : str,name : str ):
    print(name,emp_id)
    sql_query = f"""UPDATE employees 
    SET name = '{name}'
    WHERE emp_id = '{emp_id}';"""
    try:
        cursor.execute(sql_query)
        sql.commit()
    except Exception as e:
        
        print(e)
    else:
        print("Record Updated Successfully !")
    return None
    # return templates.TemplateResponse("update_name.html",{"request":request})

@router.get("/delete_emp")
async def delete_emp(request: Request):
    result = []
    sql_query = "SELECT * FROM employees;"
    try:
        cursor.execute(sql_query)
    except Exception as e:
        print(e.__context__)
    else:
        values = cursor.fetchall()
        result = list_serial(values)

    return templates.TemplateResponse("delete_emp.html",{"request": request,"employees":result})

@router.delete("/delete_emp/{emp_id}",response_class= HTMLResponse)
async def delete_record(request: Request, emp_id: str):
    print(emp_id)
    sql_query = f"DELETE FROM employees WHERE emp_id = '{emp_id}';"
    try:
        cursor.execute(sql_query)
        sql.commit()
    except Exception as e:
        print(e)
    else:
        sql.commit()
        print("Record deleted Successfully")

    return templates.TemplateResponse("delete_emp.html",{"request": request})

