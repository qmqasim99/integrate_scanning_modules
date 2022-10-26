
from fastapi import FastAPI
import redis 
import json
import os
from app.worker.modules.sublister import sublister_wrapper
from app.worker.modules.amass_runner import amass_wrapper

app = FastAPI()
rd = redis.from_url('redis://redis:6379', decode_responses=True)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/scan/")
async def get_scan(url: str):

    if(rd.exists(url)):
        print('key exists')
        return json.loads(rd.get(url))
    else:
        # sublister_result = sublister_wrapper(url)
        amass_result = amass_wrapper(url)
        result = {'scan_result': {'sublister': 'sublister_result', 'amass': amass_result}}

        # save the result in Redis
        rd.set(url, json.dumps(result))
        rd.expire(url, 60)
        return result
    

@app.get("/scan/{scan_id}")
async def get_scan(scan_id: int):
    return {"scan_id": scan_id}


@app.get("/amass_scan/")
async def get_scan(url: str):
    result = amass_wrapper(url)
    return result

    