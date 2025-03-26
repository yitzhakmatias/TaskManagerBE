import json
from tasks.utils import tasks_collection

def handler(event, context):
    task_id = event['pathParameters']['id']

    result = tasks_collection.delete_one({"_id": task_id})

    if result.deleted_count == 0:
        return {
            "statusCode": 404,
            "body": json.dumps({"error": "Task not found"})
        }

    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Task deleted"})
    }
