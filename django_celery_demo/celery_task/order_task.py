
from celery_task.celery import app
@app.task
def order_add(x,y):
    import time
    time.sleep(1)
    return x+y
