lst=['hello','world','python']
print('原列表',lst,id(lst))
# 增加元素的操作
lst.append('sql')
print('增加元素后',lst,id(lst))
# 使用insert(index,x)在指定的index位置插入元素x
lst.insert(1, 100)
print(lst)

# 列表元素的删除操作
lst.remove('world')
print('删除元素之后的列表‘',lst,id(lst))

# # 清除列表中所有的元素clear
# lst.clear()
# print(lst,id(lst))

# 列表的反向
lst.reverse()#不会产生新的列表，在原列表的基础上
print(lst)
print('-'*50)
# 列表的拷贝，将产生一个新的列表对象
new_lst=lst.copy()
print(lst,id(lst))
print(new_lst,id(new_lst))

# 列表元素的修改操作
# 根据索引进行元素
lst[1]='mysql'
print(lst)