i

import requests
import json
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

headers = {
    'accept': 'application/vnd.printdeal-api.v2',
    'User-ID': os.getenv('MY_USER_ID'),
    'API-Secret': os.getenv('MY_API_SECRET'),
}

response = requests.get('https://api.printdeal.com/api/products/8ee0c86e-8d77-4b65-93fc-fc829caf2cd5/combinations', headers=headers)

Data = response.text

parsed = json.loads(Data)
json.dumps(parsed, indent=4)

products = {}
for dic in parsed:
    for product in dic:
        products.update(dic[product])
    print(products)
