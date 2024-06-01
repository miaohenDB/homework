lst=['hello','world',98,100.5]
print(lst)

# 可以使用内置函数list()创建列表
lst2=list('helloword')
lst3=list(range(1,10,2))
print(lst2)
print(lst3)
print(lst+lst2+lst3)
print(len(lst))
print(max(lst3))
print(min(lst3))

print(lst2.count('o'))
print(lst2.index('o'))
# 列表删除操作
lst4=[10,20,30]
print(lst4)
# 删除列表
del lst4
print(lst4)
