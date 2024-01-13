import os
import chardet as chardet

# 指定文件路径
path = r'语料txt'

# 对路径内的每一个文件进行转换
for file in os.listdir(path):
  with open(os.path.join(path, file), 'rb') as f:
    # 读取文件内容
    content = f.read()
    # 判断文件内容，并进行解码
    coding = chardet.detect(content)['encoding']
    if coding != 'utf-8':
      try:
        content = content.decode(coding)
        content = content.encode('utf-8')
        # 以utf-8格式覆写文件内容
        with open(os.path.join(path, file), 'wb') as f_utf8:
          f_utf8.write(content)
      except:
        # 对于不能解码的文件会抛出异常，此处可以自行处理
        pass