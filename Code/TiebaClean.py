import os
import re

target_dir = r""

for root,dirs,files in os.walk(target_dir):
    for file in files:
        if '贴吧' in file and file.endswith('.txt'):
            txt_path = os.path.join(root,file)

            with open(txt_path,'r+',encoding='utf-8') as f:
                content = f.read()
                content = re.sub(r'https://gsp0.baidu.com/5aAHeD3nKhI2p27j8IqW0jdnxx1xbK/tb/editor/images/client/image_.*?\.png','',content)
                content = re.sub(r'回复.*?:','',content)
                content = re.sub(r'http://[a-zA-Z0-9.?%-_/&=:]*', '', content)
                f.seek(0)
                f.write(content)
                f.truncate()

print("代码运行完成！")
