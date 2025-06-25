def apiResponse(data=None, message="Success", status=200, error=None):
    return {
        "status": status,
        "message": message,
        "data": data,
        "error": error
    }