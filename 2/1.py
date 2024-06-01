s = 'helloworld'
# for i in range(0,len(s)):
#     print(i,s[i],end='\t\t')
#
# print('\n'+'-'*40)
#
# for i in range(-10,0):
#     print(i,s[i],end='\t')
# s1 = s[0:5:2]
# print(s1)
# #省略开始位置
# print(s[:5:1])
# #省略结束位置
# print(s[0:7:1])
# #省略步长
# print(s[:6:])
# #省略开始位置、结束位置、步长
# print(s[::])

print(s[::-1])
print(s[-1:-11:-1])
print('-'*40)
print(s[4:-11:-1])
# 从0开始，向后方逆序步长为1输出，因为0左侧没有数值，所以为空
print(s[0:10:-11])
print('-'*40)
print(s[4:-11:-1])