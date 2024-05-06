from typing import List

def individual_serial(todo) -> dict:
    dictionary = {
        "emp_id" : todo[0],
        "name" : todo[1],
        "email" : todo[2],
        "mobile" : todo[3],
        "department" : todo[4]
    }
    return dictionary

def list_serial(todos) -> List[dict]:
    output = [individual_serial(todo) for todo in todos]
    return output