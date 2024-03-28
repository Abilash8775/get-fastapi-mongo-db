from fastapi import APIRouter
from models.todos import Todo,Find
from config.database import collection_name
from schemas.schemas import list_serial
from bson import ObjectId

router=APIRouter()

@router.get("/")
async def get_todos():
    todos=list_serial(collection_name.find())
    if todos:
        return todos
    else:
        return "UNKNO"
@router.post("/post")
async def post_todo(todo:Todo):
    collection_name.insert_one(dict(todo))
    
@router.put("/{id}")
async def todos_put(id:str,todo:Todo):
    collection_name.find_one_and_update({"_id":ObjectId(id)},{'$set':dict(todo)})
@router.get("/one")
async def get_one(name:str):
    todos=list_serial(collection_name.find({"name":name}))
    return todos