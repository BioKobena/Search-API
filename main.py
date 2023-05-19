from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")

def index():
    return {"message" : "Hello world"}



@app.get("/items")

def get_items():
    return [
        {"id": 1, "name": "item1"},
        {"id": 2, "name": "item2"},
        {"id": 3, "name": "item3"},
        {"id": 4, "name": "item4"},
    ]


if __name__ =='__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)