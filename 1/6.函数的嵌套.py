# 函数的嵌套"""
"""def func_b():
    print('----2----')

def func_a():
    print('----1----')
    func_b()
    print('----3----')

#调用函数func——a
func_a()


# 一个用法
def fun1(x,y):
    print("这是函数一")
    sum=x+y
    return  sum
# 一个用法
def fun2():
    print("这是函数二")
    sum=fun1(2,3)
    print(sum)
fun2()"""
def max(x,y):
    return x if x>y else y

def maxs(a,b,c,d):
    res1=max(a,b)
    res2 = max(res1, c)
    res3 = max(res2, d)
    return res3
print(maxs(5,2,420,299))

# def f1():
#     def f2():
#         def f3():
#                  pass
#     print('----->f1')
    # f2()#会报错嵌套函数在外部不能使用

