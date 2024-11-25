import json
import boto3

def lambda_handler(event, context):

    user_id = event["user_id"]
    reel_id = event["reel_id"]
    action = event["action"]

    if not all([user_id, reel_id, action]):
        return {
            "statusCode": 400,
            "body": json.dumps({"message": "Missing required fields"})
        }

    send_to_kinesis(
        data={"user_id": user_id, "reel_id": reel_id, "action": action},
        partition_key=user_id+reel_id
    )

    return {
        "statusCode": 200,
        "body": {
            "message": "Interaction processed successfully",
            "data": {
                "user_id": user_id,
                "reel_id": reel_id,
                "action": action
            }
        }
    }

def send_to_kinesis(data, partition_key):
    kinesis = boto3.client('kinesis')
    data = {
      "user_id": "068a4d2a-2593-46d4-ad9d-325235f8555d",
      "reel_id": "e449b8cc-3c82-45f8-8f87-76433582e382",
      "action": "comment"
    }
    try:
        response = kinesis.put_record(
            StreamName="ReelsInteractionsStream",
            Data=json.dumps(data),  # Convert dict to JSON string
            PartitionKey=partition_key
        )
    except Exception as e:
        print("Error sending data to Kinesis:", e)
        
send_to_kinesis(1234, "12341")
