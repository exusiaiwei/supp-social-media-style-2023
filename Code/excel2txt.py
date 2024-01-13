import os
import xlrd

input_path = ""
output_path = ""

for root, dirs, files in os.walk(input_path):
    for file in files:
        if os.path.splitext(file)[1] == ".xlsx":
            file_name = root + "\\" + file
            book = xlrd.open_workbook(file_name)
            sheet = book.sheet_by_index(0)
            # 不包括k1列
            for row in range(1, sheet.nrows):
                with open(output_path + '\\' + os.path.splitext(file)[0] + ".txt", 'a', encoding="utf-8") as f:
                    f.write(str(sheet.cell(row, 10).value) + '\n')
            print("{} 已完成".format(os.path.splitext(file)[0]))