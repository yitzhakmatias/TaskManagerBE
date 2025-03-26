import json

from tasks.cors_handler import get_cors_headers
from tasks.utils import tasks_collection


def handler(event, context):
    tasks = list(tasks_collection.find())
    headers = get_cors_headers()
    for task in tasks:
        task['id'] = str(task['_id'])
        del task['_id']
    return {
        "statusCode": 200,
        "body": json.dumps(tasks),
        'headers': headers
    }
