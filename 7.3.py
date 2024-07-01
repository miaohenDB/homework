# from time import time,sleep,perf_counter
# from time import *
# a = time()
# print(a)
# sleep(10)
# b = time()
# print(b)
# print(b-a)
# # for x in range(100000):
# #     pass
# # b= time()-a
# # print(b)
# print(perf_counter())
# print(perf_counter())
# print(perf_counter())
#
# print(gmtime())
# print(localtime())
#
# print('-'*50)
# from calendar import *
# thismonth = month(2024,6,2)
# print(thismonth)
# with open('2.txt','w') as f:
#     for i in range(100):
#         print(i,file=f)


f = open('2.txt','r')
# for line in f:
#     print(line, end='')
# contents = f.readline()
# print(contents)
with open('2.txt','r') as f:
    contents = f.readlines()
    print(contents)
f.close()