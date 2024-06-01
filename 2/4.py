lst=['hello','world','python','php']
# # 使用for循环遍历列表元素
# for item in lst:
#     print(item)
#
# # 使用for循环，range()函数，len()函数，根据索引进行遍历
# for i in range(0,len(lst)):
#     print(i,'-->',lst[i])
print('-'*50)
# 第三种遍历方式enumearte()函数
for index,item in enumerate(lst):
    print(index,'-->',item)
print('-' * 50)
# 手动修改序号的起始值
for index,item in enumerate(lst,start=1000):
    print(index,'-->',item)
print('-'*50)
for index,item in enumerate(lst,1000000):#省略start不写，直接写起始值
    print(index,'-->',item)