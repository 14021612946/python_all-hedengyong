import xlrd
'''
    1.安装与导入xlrd模块（读取excel）
'''
# 1.打开工作薄并获取句柄
data =  xlrd.open_workbook("F:\\测试开发-python3\\day10\\a.xlsx")

# 2.从工作薄里选中选项卡
sheet = data.sheet_by_name("用户管理")

# 3.
print("有",sheet.nrows,"行数据！有",sheet.ncols,"列数据！")
rows = sheet.nrows # 获取所有行数
cols = sheet.ncols # 获取所有列数
f = open("用户管理.txt","w",encoding="utf-8") # 打开一个文件用于写入数据
a = [] # [张三,56,男,1352648187]
# 4.遍历所有数据
for i in range(rows):
    a = []
    for j in range(cols):
        a.append(str(sheet.cell_value(i,j)).replace(".0",""))
    string = ",".join(a) # "张三:56:男:13552648187" # 将数据用,组合成字符串
    f.write(string + "\n") # 写入到文件中






























