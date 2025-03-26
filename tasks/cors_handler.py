def get_cors_headers():
    """
    Returns the CORS headers for API Gateway to allow cross-origin requests.
    """
    return {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',  # You can change '*' to a specific domain for security
        'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE',  # Allow specific methods
        'Access-Control-Allow-Headers': 'Content-Type, Authorization',  # Allow necessary headers
    }
