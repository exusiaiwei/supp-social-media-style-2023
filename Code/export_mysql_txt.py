import os
import pymysql

# 设置数据库连接信息
host = 'localhost'
user = ''
password = ''

# 连接到MySQL数据库
db = pymysql.connect(host=host, user=user, password=password)

# 获取数据库列表
cursor = db.cursor()
cursor.execute("SHOW DATABASES")

# 遍历数据库列表，找到包含'comment', 'post', 'thread'三个表的数据库
for db_name in cursor.fetchall():
    db_name = db_name[0]
    cursor.execute(f"USE {db_name}")
    cursor.execute("SHOW TABLES")
    tables = [row[0] for row in cursor.fetchall()]
    if sorted(tables) == ['comment', 'post', 'thread']:
        # 创建导出文件夹
        path = f'/tmp/{db_name}/'
        if not os.path.isdir(path):
            os.makedirs(path)

        # 导出post表
        cursor.execute(
            f"SELECT content FROM post INTO OUTFILE '{path}{db_name}-post.txt'"
        )

        # 导出comment表
        cursor.execute(
            f"SELECT content FROM comment INTO OUTFILE '{path}{db_name}-comment.txt'"
        )

# 关闭游标和数据库连接
cursor.close()
db.close()