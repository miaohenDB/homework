def sum(*nums):
    # 定义一个变量，保存结果
    result=0
    # 遍历元祖，并将元祖中的数组进行累加
    for n in nums:
        result+=n
        print(result)

sum(12,78,90,67)
sum(10,20,30,)
sum(123,456,789,10,20,30,40)