import json

# import requests


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    event: dict, required
    context: object, required

    Returns
    API Gateway Lambda Proxy Output Format: dict
    """

    # try:
    #     ip = reque
    # sts.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Heck you mean? I'm working!",
            # "location": ip.text.replace("\n", "")
        }),
    }
