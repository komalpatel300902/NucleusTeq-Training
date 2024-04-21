from fastapi import APIRouter
from config.databases import sql , cursor
from model.models import Register
from schema.schema import list_serial

router = APIRouter()

@router.post("/")
async def enter_employee_details(info : Register):
    sql_query = f"INSERT INTO employees VALUES ('{info.emp_id}','{info.name}','{info.email}','{info.mobile}','{info.department}');"
    try:
        cursor.execute(sql_query)
    except Exception as e:
        print(e)
    else:
        sql.commit()
        print("Record added successfully !!!")

@router.get("/my_info")
async def my_info():
    result = []
    sql_query = "SELECT * FROM employees;"
    try:
        cursor.execute(sql_query)
    except Exception as e:
        print(e.__context__)
    else:
        values = cursor.fetchall()
        result = list_serial(values)

    return result

@router.put("/{emp_id}")
async def update_name(emp_id : str,name : str):
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

@router.delete("/")
async def delete_record(emp_id:str):
    sql_query = f"DELETE FROM employees WHERE emp_id = '{emp_id}';"
    try:
        cursor.execute(sql_query)
        sql.commit()
    except Exception as e:
        print(e)
    else:
        sql.commit()
        print("Record deleted Successfully")


