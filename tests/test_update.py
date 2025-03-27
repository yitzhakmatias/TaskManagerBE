# tests/test_update.py
import json
from tasks.update_task import handler

def test_update_task():
    event = {
        'pathParameters': {'id': 'dummy-task-id'},
        'body': json.dumps({'status': 'in_progress'})
    }
    context = {}

    response = handler(event, context)

    assert response['statusCode'] == 200
    body = json.loads(response['body'])
    assert body['message'] == 'Task updated'
