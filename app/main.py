from fastapi import FastAPI
from app.worker.modules.sublister import sublister_wrapper

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/scan/")
async def get_scan(url: str):
    result = sublister_wrapper(url)
    return result

@app.get("/scan/{scan_id}")
async def get_scan(scan_id: int):
    return {"scan_id": scan_id}


    