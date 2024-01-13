import re

   # 读取文本文件并存储为字符串
with open(r'', 'r', encoding='utf-8') as f:
       text = f.read()

   # 构造正则表达式，用于匹配前后都有带“一”的相同词语的句子
pattern = re.compile(r'.*一.+一.+(.+)(?<=一\1一).*')

   # 使用正则表达式搜索文本文件
sentences = pattern.findall(text)

for sentence in sentences:
    print(sentence)