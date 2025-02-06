import pandas as pd
import requests
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

def parser_product(json):
    d = dict()
    d['product_id'] = json.get('id')
    d['name'] = json.get('name')
    d['price'] = json.get('original_price')
    
    # Extract categories from the breadcrumbs field
    breadcrumbs = json.get('breadcrumbs', [])
    if breadcrumbs:
        category1 = breadcrumbs[1] if len(breadcrumbs) > 0 else {}
        category2 = breadcrumbs[2] if len(breadcrumbs) > 1 else {}
        d['category1_id'] = category1.get('category_id', None)
        d['category1_name'] = category1.get('name', None)
        d['category2_id'] = category2.get('category_id', None)
        d['category2_name'] = category2.get('name', None)
    
    quantity_sold = json.get('quantity_sold')
    d['quantity_sold'] = quantity_sold.get('value') if quantity_sold else None
    d['review_count'] = json.get('review_count')
    d['rating_average'] = json.get('rating_average')
    d['description'] = json.get('description')
    return d

def images_parser(json):
    d = dict()
    d['product_id'] = json.get('id')
    # Kiểm tra sự tồn tại của 'images'
    images = json.get('images', [])
    for i, image in enumerate(images[:5]):
        d[f'image_{i+1}'] = image.get('base_url')
    return d

df_id = pd.read_csv('TIKI/product_id.csv')
p_ids = df_id.product_id.to_list()[0:]
print(p_ids)

product = []
image = []
for pid in tqdm(p_ids, total=len(p_ids)):
    response = requests.get(f'https://tiki.vn/api/v2/products/{pid}', headers=headers, params=params)
    if response.status_code == 200:
        json_data = response.json()
        if json_data:
            print(f'Crawl data {pid} success !!!')
            product.append(parser_product(json_data))
            image.append(images_parser(json_data))
        else:
            print(f'No data found for product ID: {pid}')
    time.sleep(random.randrange(1, 3))

df_product = pd.DataFrame(product)
df_product.to_csv('product_data.csv', mode='a', index=False, header=False)
df_image = pd.DataFrame(image)
df_image.to_csv('images.csv', mode='a', index=False, header=False)
