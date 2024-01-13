import pandas as pd

# 读取Excel文件
df = pd.read_excel("", sheet_name=0)

# 选取URL列，批量删除/answer及之后的部分
df['Url'] = df['Url'].apply(lambda x: x.split('/answer')[0])

# 保存Excel文件
df.to_excel("", sheet_name='Sheet1')