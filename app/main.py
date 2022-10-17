from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/scan/{scan_id}")
async def get_scan(scan_id: int):
    return {"scan_id": scan_id}

    