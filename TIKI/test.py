import pandas as pd
import random
from faker import Faker

# Bước 1: Tạo danh sách user_id từ KH0005 đến KH0016
user_ids = [f"KH{str(i).zfill(4)}" for i in range(5, 17)]  # KH0005 đến KH0016

# Bước 2: Đọc file products.csv để lấy danh sách product_id
products_df = pd.read_csv(r"C:\Users\anhn2\Documents\DATN\clothing_store_BE\data\products.csv")  # Đảm bảo rằng file này có cột 'product_id'
product_ids = products_df['product_id'].tolist()  # Lấy danh sách product_id từ file products.csv

# Bước 3: Tạo dữ liệu review
reviews = []

# Tạo 1 review cho mỗi user_id, mỗi user_id đánh giá ngẫu nhiên từ 1 đến 30 sản phẩm
for user_id in user_ids:
    num_reviews = random.randint(1, 30)  # Số lượng sản phẩm người dùng sẽ đánh giá từ 1 đến 30
    
    # Tạo num_reviews đánh giá cho mỗi user_id
    for _ in range(num_reviews):
        product_id = random.choice(product_ids)
        
        # Tạo rating ngẫu nhiên với xu hướng nghiêng về 4-5 sao
        rating = random.choices([1, 2, 3, 4, 5], weights=[5, 5, 10, 30, 50])[0]  # Lớn hơn là có khả năng cao hơn

        # Tạo comment ngẫu nhiên tùy theo rating
        if rating == 5:
            comment = "Sản phẩm tuyệt vời, tôi rất hài lòng!"
        elif rating == 4:
            comment = "Sản phẩm tốt, nhưng có thể cải thiện một số chi tiết nhỏ."
        elif rating == 3:
            comment = "Sản phẩm ổn, nhưng không quá ấn tượng."
        elif rating == 2:
            comment = "Sản phẩm không như mong đợi, có thể cải thiện nhiều hơn."
        else:
            comment = "Rất thất vọng, sản phẩm không đạt yêu cầu."

        # Lưu review vào danh sách
        reviews.append([user_id, product_id, rating, comment])

# Bước 4: Chuyển danh sách reviews thành DataFrame
review_df = pd.DataFrame(reviews, columns=['user_id', 'product_id', 'rating', 'comment'])

# Thêm cột review_id tăng dần bắt đầu từ 1
review_df['review_id'] = range(1, len(review_df) + 1)

# Bước 5: Sắp xếp lại thứ tự các cột
review_df = review_df[['review_id', 'user_id', 'product_id', 'rating', 'comment']]

# Bước 6: Lưu kết quả vào file CSV
review_df.to_csv(r"C:\Users\anhn2\Documents\DATN\clothing_store_BE\data\review.csv", index=False)

# Hiển thị dữ liệu đầu ra (hoặc kiểm tra trực tiếp trong file review.csv)
print(review_df.head())
