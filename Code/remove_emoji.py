import os
import re

# 指定文件夹
directory = r''
# 遍历文件夹中的文件
for file in os.listdir(directory):
    # 如果是txt文件
    if file.endswith(".txt"):
        # 读取文件
        with open(directory+'/'+file, 'r', encoding='utf-8') as f:
            input_text = f.read()
        # 删除所有emoji符号
        output_text = re.sub(u'[\U00010000-\U0010ffff]', '', input_text)
        # 写入文件
        with open(directory+'/'+file, 'w', encoding='utf-8') as f:
            f.write(output_text)