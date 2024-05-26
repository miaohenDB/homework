#
"""def factorial(n):
    if n==1:
        return 1#边界
    else:
        return n*factorial(n-1)#递归函数
num=5
#测试
result=factorial(num)
print(f'The factorial of{num}is:{result}')"""
#从n到n/2-1到(n/2-1)/2-1到....到n=1
# 第一天摘下若干个桃子，当即吃了一半，又多吃了一个;
# 第二天将剩下的桃子吃掉一半，又多吃1个;
# 后面每天均是如此，到第n天想吃时，只剩下1个。计算猴子第一天共摘了多少个桃子。
n=int(input('请输入n的值：'))#开始时候n的值第n天时n=1
def F(x):
    if x==1:
        return x#边界
    else:
        return (F(x-1)+1)*2
print(F(n))#输出递归值