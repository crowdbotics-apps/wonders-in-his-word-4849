import json


def hello(event, context):
    body = {
        "message": "Congratulations! You just released your first serverless function - wonders_in_his_word_4849 - with Crowdbotics! Reward yourself! Grab a cup of coffee!"
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
