# i=1
# while i<100:
#     print(i)
#     i=i*2
i = 0
while i < 3:
 score = int(input("请输入您的分数"))
 if score <= 100 and score >= 90:
    print("优秀")
 elif score < 90 and score >= 80:
     print("良好")
 elif score < 80 and score >= 70:
     print("还行")
 elif score < 70 and score >= 60:
     print("一般般")
 elif score < 60:
     print("不及格")
 else:
     print("输入非法")
 i = i + 1











