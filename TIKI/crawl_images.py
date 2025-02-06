import pandas as pd
import requests # type: ignore
import time
import random
from tqdm import tqdm # type: ignore

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'vi,en;q=0.9,vi-VN;q=0.8,fr-FR;q=0.7,fr;q=0.6,en-US;q=0.5',
    'x-guest-token': 'dw6s3DtQ4zvCaTFOBExp5YHrmqk0Kjeg',
}

params = (
    ('platform', 'web'),
    ('spid', 102093966),
    ('version', 3)
)

def images_parser(json):
    d = dict()
    d['product_id'] = json.get('id')
    # Kiểm tra sự tồn tại của 'images'
    images = json.get('images')
    images = json.get('images', [])
    for i, image in enumerate(images[:5]):
        d[f'image_{i+1}'] = image.get('base_url')
    return d


df_id = pd.read_csv('TIKI/product_id.csv')
p_ids = df_id.product_id.to_list()
print(p_ids)
result = []
for pid in tqdm(p_ids, total=len(p_ids)):
    response = requests.get('https://tiki.vn/api/v2/products/{}'.format(pid), headers=headers, params=params,)
    if response.status_code == 200:
        json_data = response.json()
        if json_data:
            print('Crawl data {} success !!!'.format(pid))
            result.append(images_parser(json_data))
        else:
            print('No data found for product ID: {}'.format(pid))
    time.sleep(random.randrange(1, 3))

df_product = pd.DataFrame(result)
df_product.to_csv('TIKI/images.csv', mode='a', index=False, header=False)

