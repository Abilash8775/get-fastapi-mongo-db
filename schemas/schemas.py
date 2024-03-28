def individual_serial(todo) -> dict:
    return{
        'id':str(todo["_id"]),
        'name':todo["name"],
        'mobile':todo["mobile"],
        'email':todo["email"]
    }
    
def list_serial(todos) ->list:
    return[individual_serial(todo) for todo in todos]