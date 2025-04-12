import requests,asyncio,config,json;

HEADERS = {
    "X-Key":f"{config.API_KEY}",
    "X-Secret" : f"{config.SECRET_KEY}"
}

URL = 'https://api-key.fusionbrain.ai/'

async def generate(prompt):
    params = {
        "type": "GENERATE",
        "numImages": 1,
        "width": 1024,
        "height":1024,
        "generateParams": {"query": prompt}
    }
    files = {
        "mode_id": (None , 4),
        "params" : (None, json.dumps(params), "application/json")
    }
    response = requests.post(URL + "key/api/v1/text2image/run/", headers=HEADERS,files=files)
    data = response.json()
    attempts = 0
    
    while (attempts < 40):
        response = requests.get(URL + "key/api/v1/text2image/status/" + data["uuid"],headers=HEADERS)
    data = response.json()
    if data["status"] == "DONE":
        return data["images"]
    attempts += 1
    await asyncio.sleep(3)