import json

from tasks.cors_handler import get_cors_headers
from tasks.utils import tasks_collection

def handler(event, context):
    task_id = event['pathParameters']['id']

    result = tasks_collection.delete_one({"_id": task_id})
    headers = get_cors_headers()
    if result.deleted_count == 0:
        return {
            "statusCode": 404,
            "body": json.dumps({"error": "Task not found"})
        }

    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Task deleted"}),
        'headers': headers
    }
