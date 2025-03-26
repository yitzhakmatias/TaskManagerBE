import json
from tasks.utils import tasks_collection

def handler(event, context):
    task_id = event['pathParameters']['id']
    data = json.loads(event['body'])

    if 'status' not in data:
        return {
            "statusCode": 422,
            "body": json.dumps({"error": "Missing status"})
        }

    result = tasks_collection.update_one(
        {"_id": task_id},
        {"$set": {"status": data['status']}}
    )

    if result.matched_count == 0:
        return {
            "statusCode": 404,
            "body": json.dumps({"error": "Task not found"})
        }

    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Task updated"})
    }
