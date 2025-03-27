# tests/test_get.py
import json
from tasks.get_tasks import handler

def test_get_tasks():
    event = {}  # Puedes simular eventos de API Gateway
    context = {}

    response = handler(event, context)

    assert response['statusCode'] == 200
    assert 'body' in response
    tasks = json.loads(response['body'])
    assert isinstance(tasks, list)
