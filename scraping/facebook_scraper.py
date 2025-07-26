# # scraping/facebook_scraper.py

# def scrape_facebook():
#     print("📘 [Facebook] เริ่มดึงข้อมูลโพสต์/รีวิวจากเพจ...")
    
#     # TODO: ใช้ Facebook Graph API หรือ scraping (ขึ้นกับ token & สิทธิ์)
#     # ด้านล่างเป็น mockup สำหรับทดสอบ

#     posts = [
#         {"author": "ลูกค้า A", "comment": "เตาดีมาก ส่งไว", "likes": 12},
#         {"author": "ลูกค้า B", "comment": "ใช้แล้วประหยัดแก๊ส", "likes": 7},
#     ]

#     for p in posts:
#         print(f"{p['author']} → 💬 {p['comment']} ❤️ {p['likes']} likes")

#     print("✅ [Facebook] ดึงข้อมูลสำเร็จ")
#     return posts
def scrape_facebook():
    print("เริ่มดึงข้อมูล facebook (mock)...")
    # mock data จำลองรีวิวสินค้า
    mock_reviews = [
        {"product_id": "1234", "review": "สินค้าดีมาก", "rating": 5, "author": "ลูกค้า A"},
        {"product_id": "5678", "review": "ส่งช้าไปนิด", "rating": 3, "author": "ลูกค้า B"},
    ]
    print(f"ดึงข้อมูล facebook mock เสร็จ: {len(mock_reviews)} รีวิว")
    return mock_reviews
