from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def first_api():
    """_summary_: First API
    _description_: This is the first API
    _returns_: This is the first API
    """
    return {"message": "Hello Jensen!"}
