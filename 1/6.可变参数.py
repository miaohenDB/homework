#位置传递
def use_info(*args):
    print(args)


#("TOM",)
use_info('TOM')
#("TOM",18)
use_info('TOM',18)

#关键字传递
def user_info1(**kwargs):
    print(kwargs)

# {'name':'TOM','age':18,'id':100}
user_info1(name="TOM",age='18',id=110)#参数是键=值形式