import json
import uuid

from tasks.cors_handler import get_cors_headers
from tasks.utils import tasks_collection

def handler(event, context):
    data = json.loads(event['body'])

    if 'title' not in data or 'description' not in data:
        return {
            "statusCode": 422,
            "body": json.dumps({"error": "Missing title or description"})
        }
    headers = get_cors_headers()
    task = {
        "_id": str(uuid.uuid4()),
        "title": data['title'],
        "description": data['description'],
        "status": "todo"
    }
    tasks_collection.insert_one(task)
    return {
        "statusCode": 201,
        "body": json.dumps({"message": "Task created"}),
        'headers': headers
    }
