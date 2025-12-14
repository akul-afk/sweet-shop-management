import pymysql

try:
    conn = pymysql.connect(
        host="127.0.0.1",
        user="sweet_user",
        password="Sweet123",
        database="sweet_shop",
        port=3306
    )
    print("✅ Connected OK")
    conn.close()
except Exception as e:
    print("❌ Error:", e)
