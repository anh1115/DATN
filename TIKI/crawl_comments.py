import requests
import pandas as pd
from tqdm import tqdm

# Định nghĩa cookies và headers
cookies = {
    "TOKENS": "{%22access_token%22:%22dw6s3DtQ4zvCaTFOBExp5YHrmqk0Kjeg%22}",
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'vi,en;q=0.9',
    'x-guest-token': 'dw6s3DtQ4zvCaTFOBExp5YHrmqk0Kjeg',
    }

params = {
    'limit': '5',
    'include': 'comments,contribute_info,attribute_vote_summary',
    'sort': 'score|desc,id|desc,stars|all',
    'page': '1',
    'spid': '102093966',
    'product_id': '102093936',
}

def comment_parser(json):
    d = dict()
    d['customer_id'] = json.get('customer_id')
    d['product_id'] = json.get('product_id')
    d['rating'] = json.get('rating')
    return d
    

# Đọc danh sách product ID từ file CSV
df_id = pd.read_csv('TIKI/product_id.csv')
p_ids = df_id.product_id.to_list()
result = []

for pid in tqdm(p_ids, total=len(p_ids)):
    params['product_id'] = pid
    print(f'Crawl comment for product {pid}')
    
    current_page = 1  # Biến theo dõi trang hiện tại

    while True:  # Vòng lặp vô hạn, sẽ dừng khi không còn trang nữa
        params['page'] = current_page
        response = requests.get('https://tiki.vn/api/v2/reviews', headers=headers, params=params, cookies=cookies)
        
        if response.status_code == 200:
            data = response.json()
            print(f'Crawl comment page {current_page} success!!!')
            
            # Thêm các comment vào kết quả
            for comment in data.get('data', []):
                result.append(comment_parser(comment))

            # Kiểm tra xem có còn trang nữa không
            total_pages = data.get('paging', {}).get('last_page', 0)
            if current_page < total_pages:
                current_page += 1  # Tăng số trang hiện tại lên 1
            else:
                break  # Dừng lại nếu đã lặp qua hết tất cả các trang
        else:
            print(f'Error: {response.status_code} - {response.text}')
            break  # Dừng lại nếu có lỗi trong phản hồi

# Chuyển đổi kết quả thành DataFrame và lưu vào CSV
df_comment = pd.DataFrame(result)
df_comment.to_csv('TIKI/review.csv', mode='a', index=False, header=False)