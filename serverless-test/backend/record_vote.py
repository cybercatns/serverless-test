import json
import boto3
import os

dynamodb = boto3.client('dynamodb')

def handler(event, context):
    result = dynamodb.scan(
        TableName = os.environ['DYNAMODB_TABLE']
    )
    song_votes = []

    for item in result["Items"]:
        song_votes.append({
            "songName" : item["songName"]["S"],
            "cost" : item["cost"]["S"]
        }) 

    response = {
        "statusCode": 200,
        "headers": {"Access-Control-Allow-Origin" : "*"},
        "body": json.dumps(song_votes)
    }

    return response
   