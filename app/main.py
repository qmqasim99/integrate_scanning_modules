
from celery.result import AsyncResult
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import redis 
import json
import os
# from app.worker.modules.sublister import sublister_wrapper
# from app.worker.modules.amass_runner import amass_wrapper
from app.celery_worker import create_task

app = FastAPI()
# rd = redis.from_url('redis://redis:6379', decode_responses=True)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/scan/")
async def get_scan(url: str):

    task = create_task.delay(url)
    return {"task_id": task.id}
    

@app.get("/scan/{scan_id}")
async def get_scan(scan_id: str):
    task_result = AsyncResult (scan_id)
    result = {
        "task_id": scan_id,
        "task_status": task_result.status,
        "task_result": task_result.result
    }
    return JSONResponse(result)


@app.get("/amass_scan/")
async def get_scan(url: str):
    result = amass_wrapper(url)
    return result

    