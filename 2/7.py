lst=[1,2,3,10,11,12,13,14,15]
print('原列表',lst)

# 排序
asc_lst=sorted(lst)
print('升序',lst)

#排序降序
desc_lst=sorted(lst,reverse=True)
print('降序',lst)

lst2=['banana','apple','Cat','Orange']
print('原列表',lst2)

# 忽略大小写进行排序
new_lst=sorted(lst2,key=str.lower)
print('排序后的列表',new_lst)