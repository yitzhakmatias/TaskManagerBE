import json
from tasks.utils import tasks_collection

def handler(event, context):
    tasks = list(tasks_collection.find())
    for task in tasks:
        task['id'] = str(task['_id'])
        del task['_id']
    return {
        "statusCode": 200,
        "body": json.dumps(tasks)
    }
