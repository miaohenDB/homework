# 这是一个全局变量
global_var = 10


def modify_global_var():
    # 使用global关键字声明我们要修改的是全局变量
    global global_var
    global_var += 5
    print("在函数内部，global_var的值为:", global_var)


# 在函数外部访问全局变量
print("在函数外部，global_var的值为:", global_var)

# 调用函数
modify_global_var()

# 再次在函数外部访问全局变量，值已经被函数修改

print("在函数外部，global_var的值为:", global_var)