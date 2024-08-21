from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()

class Item(BaseModel):
    text: str = None
    is_done: bool = False



items = []


@app.get("/") #defines a path for the http method. Our root directory is going to be /
def root():
    return {"Hello": "World"}

#create routes. To do items on the list 
@app.post("/items") #http post request 
def create_item(item: Item):
    items.append(item)
    return items

@app.get("/items", response_model= list[Item])
def list_items(limit: int = 10):
    return items[0:limit]


@app.get("/items/{item_id}", response_model= Item)
def get_item(item_id: int) -> Item:
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail=f"Item {item_id} not found")



#Command to initialize http: uvicorn main:app --reload

#------------------------Commands to run on cmd.exe--------------------------------------------------------------------


#Correct way to post item: curl -X POST -H 'Content-Type:application/json' http://127.0.0.1:8000/items?item=banana
#Correct way to get item: curl -X GET http://127.0.0.1:8000/items/0
#Correct way to post item using Item class: curl -X POST -H "Content-Type:application/json" -d "{\"text\": \"apple\"}" http://127.0.0.1:8000/items


#Another way to test api is: http://127.0.0.1:8000/docs#/