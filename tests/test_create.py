# tests/test_create.py
import json
from tasks.create_task import handler

def test_create_task():
    event = {
        'body': json.dumps({
            'title': 'New Task',
            'description': 'This is a task description'
        })
    }
    context = {}

    response = handler(event, context)

    assert response['statusCode'] == 201
    body = json.loads(response['body'])
    assert body['message'] == 'Task created'
