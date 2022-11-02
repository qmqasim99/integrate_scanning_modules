import os
import redis 
import json
from celery import Celery
from app.worker.modules.amass_runner import amass_wrapper


celery = Celery(__name__)
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379")
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND", "redis://localhost:6379")

rd = redis.from_url('redis://redis:6379', decode_responses=True)


@celery.task(name="create_task")
def create_task(url: str):
    if(rd.exists(url)):
        print('key exists')
        return json.loads(rd.get(url))
    else:
        amass_result = amass_wrapper(url)
        result = {'scan_result': {'sublister': 'sublister_result', 'amass': amass_result}}

        # save the result in Redis
        rd.set(url, json.dumps(result))
        rd.expire(url, 60)
        return result
