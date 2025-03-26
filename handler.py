import json


def hello(event, context):
    body = {
        "message": "Go Serverless v4.0! Your function executed successfully!",
    }

    response = {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "https://master.d1i13mf9g1bzc.amplifyapp.com",  # Allow requests from your Amplify app
            "Access-Control-Allow-Methods": "OPTIONS, GET, POST, PUT, DELETE",  # Allowed methods
            "Access-Control-Allow-Headers": "Content-Type, Authorization",  # Allowed headers
        },
        "body": json.dumps(body)
    }

    return response
