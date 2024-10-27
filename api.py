from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"mensaje": "Estas en el home"}

@app.get("/holamundo")
async def saludo(nombre):
    return {"message": f"Hola {nombre}"}

items = [
    {"name": "Foo"},
    {"name": "Bar"},
    {"name": "Baz"},
    {"name": "Qux"}
]

@app.get("/items/")
async def read_items():
    return items

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return items[item_id]
