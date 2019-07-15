from celery_task.celery import app
@app.task
def user_add(x,y):
    import time
    time.sleep(1)
    return x+y