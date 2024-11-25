# File: send_random_requests.py
import requests
import uuid
import random
import time

ENDPOINT_URL = "https://gqbqr2kafd.execute-api.us-east-1.amazonaws.com/dev/process-interaction"

ACTIONS = ["like", "view", "comment", "save"]
USERS_UUID = [
    '068a4d2a-2593-46d4-ad9d-325235f8555d',
    'ad930f43-df79-4464-93f8-0dbef56d3e7d',
    'a23e8d23-710a-477f-be13-4724339dfa38',
    'e664e892-527f-4ed5-89a6-bc49b7aae1fd',
    '025e0391-d964-4619-85fa-d980f97b639d',
    'bde9b2f7-3cab-4fd5-afba-1583aecb1651',
    '7ebea56a-8ec6-4c37-b3a6-60e4b7e480c8',
    '36f35951-bfe2-4458-810d-771525860d56',
    '72e96abd-e9bb-4e10-b716-b5797dd91103',
    '56da4948-04b0-4b50-a23b-a3dde218a694',
    '8fd32f4c-0d1b-4c85-8ebd-71eaa5c29d0a',
    'e1568634-270f-4b13-910d-c68746e7bc7b',
    'e498ad59-b06a-4772-9c69-36a20092af26',
    'c342daf5-92a1-44d4-9809-3d5a79525373',
    '8a425a2f-a136-4251-88e9-879717183001',
    '5fece107-35a6-4d23-b960-e0d684527b96',
    'd4eb838c-818f-4451-af66-be3b71f125c8',
    'e5593de6-e7b3-4373-a3bc-dc644ed63f31',
    '66c6443d-d49d-4722-b452-3c0089632c9a',
    'ed78a3a9-9707-4235-8fa6-db9d32157b85',
    '0cc2d3a8-22b2-4709-ba60-ac7523d91690',
    '216f042b-8c5a-40ea-922a-2f9f9c6fb12c',
    '344b5c32-afe6-44d7-8ba4-43b44336e79d',
    '5d7e43a6-ea2d-4b73-bc41-0cde494c7052',
    'f0853183-0be6-4eb5-ae61-cbaa8643d4ce',
    'db42aa7a-9793-4dca-bdfe-561721f640e7',
    'c6cb11fd-f94c-4072-b5ac-d4d031cbc34e',
    '1e510a06-9a6a-4a33-8fb2-aef656576f77',
    '3d564fe0-5d01-471f-ae6c-d448e5fbeb5e',
    'd315b0c0-b4fd-46ea-9a0d-504aaaa0c89f'
]
REELS_UUID = [
    '2a6a3834-040a-49cb-9f2b-2adbc8e33c88',
    'fb2c3ab9-3cee-47b4-8536-11543f129834',
    '41f0affb-ec0c-4e7a-926e-4afdf7ac2709',
    '1d5155a8-cd1a-4121-9cec-7d1ce1e6ccc0',
    '0ddf7639-2dd4-4091-a323-388fe95ba9e5',
    'dd742691-de8c-4206-a01a-89851fb28c3d',
    '941ef8a5-6a91-4498-b18c-9be934c04976',
    '34a04578-e31c-4ceb-856f-8a9f97018f31',
    '2c826d1e-843f-44fd-a17e-117f89131d14',
    'a3c07948-a79e-497c-8eaa-48334184d70e',
    'cab99f95-cc9e-40f4-b2f9-c3b4b0f90cfa',
    'c457ab4e-f4b0-4afe-9cbe-b11f7972de36',
    '9f84227c-2161-4a92-8793-29ee54ca38f3',
    '17e9f011-2e63-490b-a4fe-89f56aa399ab',
    'f74c3004-488d-4ffa-9ca9-03990324bff7',
    'c0a4ee9e-afc3-41d8-bed6-90fb634224fe',
    '9e3704ce-72b8-4952-813b-851631a62483',
    '5db24aac-7cb7-46cc-b0b5-1806ec990d9d',
    '434cf5e9-ecfd-4e12-9375-319d43b30e2e',
    '49884c80-daa8-4ca0-a163-038318c7d08d',
    'e449b8cc-3c82-45f8-8f87-76433582e382',
    '24084764-427f-4e3f-abe2-76c7e11a5f53',
    'ddd0af6f-e6cf-49b8-b777-6a4f1bb32b02',
    'f6bdc247-8fd9-469d-aa46-f3c33972e0b7',
    'bd06aa82-7295-47f7-8182-55e28d9686db',
    '904cd564-c729-4428-9e9f-ad2de214b7a2',
    'da90a773-709b-4fff-b5b0-83ed735086ed',
    'f91b4396-63ea-4d88-ab3e-c4383cbf9764',
    'aa5b7321-ea2e-4770-a167-9c1545e5fa03'
]

def generate_random_request():
    """
    Generates a random request payload.
    """
    return {
        "user_id": random.choice(USERS_UUID),
        "reel_id": random.choice(REELS_UUID),
        "action": random.choice(ACTIONS)
    }

def send_requests(batch_size=10, delay=1):
    """
    Sends a batch of requests to the endpoint.

    :param batch_size: Number of requests to send in a batch.
    :param delay: Delay between requests in seconds.
    """
    for _ in range(batch_size):
        payload = generate_random_request()
        try:
            response = requests.post(ENDPOINT_URL, json=payload)
            print(f"Request sent: {payload}")
            print(f"Response: {response.status_code} - {response.text}")
        except requests.RequestException as e:
            print(f"Error sending request: {e}")
        time.sleep(delay)

if __name__ == "__main__":
    # Adjust the number of requests and delay as needed
    send_requests(batch_size=5, delay=1)