# import time
# # from calendar import *
import calendar
# from time import *
#
# for x in range(0,12):
#     print(x)
#     sleep(1)
#     x += 1

# import calendar
#
# # 设置每周的起始日期为星期日
# calendar.setfirstweekday(calendar.SUNDAY)
#
# # 创建一个TextCalendar实例
# cal = calendar.TextCalendar(calendar.SUNDAY)
#
# # 遍历2024年的所有月份
# for month in range(1, 13):
#     # 打印2024年每个月的日历
#     print(cal.formatmonth(2024, month))


# # 打开文件
# with open('word.txt', 'r', encoding='utf-8') as file:
#     # 初始化计数器
#     python_count = 0
#
#     # 逐行读取文件
#     for line in file:
#         # 按空格分割单词
#         words = line.split()
#         # 统计当前行中 'python' 单词的出现次数
#         for word in words:
#             if word.lower() == 'itheima':
#                 python_count += 1
#
# # 输出统计结果
# print(f"'itheima' 单词出现的次数: {python_count}")


# students = []
# with open('3.txt', 'r', encoding='utf-8') as file:
#     for line in file:
#         parts = line.strip().split(',')
#         student_id, name, score = parts[0], parts[1], int(parts[2])
#         students.append({'id': student_id, 'name': name, 'score': score})
# students_sorted = sorted(students, key=lambda x: x['score'], reverse=True)
# for student in students_sorted:
#     print(f"学号: {student['id']}, 姓名: {student['name']}, 成绩: {student['score']}")
# 打开文件
with open('3.txt', 'r', encoding='utf-8') as file:
    # 读取所有行
    lines = file.readlines()
# 解析数据并存储在列表中
data = []
for line in lines:
    # 去掉行末的换行符并按逗号分割
    student_id, name, grade = line.strip().split(',')
    # 将成绩转换为整数
    grade = int(grade)
    # 将数据作为元组添加到列表中
    data.append((student_id, name, grade))

# 按成绩排序
sorted_data = sorted(data, key=lambda x: x[2], reverse=True)

# 输出排序后的数据
for student in sorted_data:
    print(f"学号: {student[0]}, 姓名: {student[1]}, 成绩: {student[2]}")