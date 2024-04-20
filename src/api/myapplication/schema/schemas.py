def individual_serial(todo) -> dict:
    
    return {
        "id": str(todo["_id"]),
        "name": todo["name"],
        "description": todo["description"],
        "complete" : todo["complete"]
    }

def list_serial(todos) -> list:
    a = todos
    index = 0
    for t in a:
        print(type(t))
        if index == 2:
            break
        index += 1
        
    return [individual_serial(todo) for todo in todos]