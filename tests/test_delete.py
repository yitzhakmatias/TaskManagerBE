# tests/test_delete.py
import json
from tasks.delete_task import handler

def test_delete_task():
    event = {'pathParameters': {'id': 'dummy-task-id'}}
    context = {}

    response = handler(event, context)

    assert response['statusCode'] == 200
    body = json.loads(response['body'])
    assert body['message'] == 'Task deleted'
