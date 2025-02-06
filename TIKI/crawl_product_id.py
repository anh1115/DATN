import requests # type: ignore
import time
import random
import pandas as pd # type: ignore

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'vi,en;q=0.9,vi-VN;q=0.8,fr-FR;q=0.7,fr;q=0.6,en-US;q=0.5',
    'Referer': 'https://tiki.vn/ao-thun-nu/c933?rating=4',
    'x-guest-token': 'dw6s3DtQ4zvCaTFOBExp5YHrmqk0Kjeg',
}

params = {
    'limit': '40',
    'include': 'advertisement',
    'aggregations': '2',
    'category': '933',
    'page': '1',
    'rating': '4',
    'urlKey': 'ao-thun-nu',
}

product_id = []
for i in range(1, 20):
    params['page'] = i
    response = requests.get('https://tiki.vn/api/personalish/v1/blocks/listings?', headers=headers, params=params)
    if response.status_code == 200:
        print('request success!!!')
        for record in response.json().get('data'):
            product_id.append({'id': record.get('id')})
    time.sleep(random.randrange(3, 10))

df = pd.DataFrame(product_id)
df.to_csv('TIKI/product_id.csv', mode='a', index=False, header=False)