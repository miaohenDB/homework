# business_cards = {
#     "陈旭": {"职位": "销售经理", "住址": "黑龙江能源职业学院1"},
#     "李华": {"职位": "学生", "住址": "黑龙江能源职业学院2"},
#     "李明": {"职位": "教师", "住址": "黑龙江能源职业学院3"},
#     "王书": {"职位": "工程师", "住址": "黑龙江能源职业学院4"},
#     # ... 可以继续添加其他名片信息
# }
# def find_contact_info():
#     """根据用户输入的姓名查找职位和住址"""
#     name = input("请输入姓名（输入'q'退出）: ")
#     if name.lower() == 'q':  # 检查是否输入了退出命令
#         print("退出名片管理系统。")
#         return False  # 返回False以退出循环
#     if name in business_cards:
#         contact_info = business_cards[name]
#         print(f"姓名: {name}")
#         print(f"职位: {contact_info['职位']}")
#         print(f"住址: {contact_info['住址']}")
#     else:
#         print(f"未找到名为 {name} 的名片信息。")
#     return True  # 返回True以继续循环
#
# # 使用无限循环来不断获取用户输入
# while True:
#     if not find_contact_info():
#         break  # 如果用户输入了退出命令，则退出循环
# 名片信息字典
business_cards = {
        "陈旭": {"职位": "销售经理", "住址": "黑龙江能源职业学院1"},
        "李华": {"职位": "学生", "住址": "黑龙江能源职业学院2"},
        "李明": {"职位": "教师", "住址": "黑龙江能源职业学院3"},
        "王书": {"职位": "工程师", "住址": "黑龙江能源职业学院4"},
    # ... 其他名片信息
}


def add_contact_info():
    """添加新的名片信息"""
    name = input("请输入姓名: ")
    if name in business_cards:
        print("该姓名已存在，请重新输入。")
        return
    position = input("请输入职位: ")
    address = input("请输入住址: ")
    business_cards[name] = {"职位": position, "住址": address}
    print(f"已添加 {name} 的名片信息。")


def find_contact_info():
    """根据用户输入的姓名查找职位和住址"""
    name = input("请输入姓名（输入'q'退出）: ")
    if name.lower() == 'q':
        print("退出名片管理系统。")
        return False
    if name in business_cards:
        contact_info = business_cards[name]
        print(f"姓名: {name}")
        print(f"职位: {contact_info['职位']}")
        print(f"住址: {contact_info['住址']}")
    else:
        print(f"未找到名为 {name} 的名片信息。")
    return True
def list_all_contacts():
    """列出所有人的名片信息"""
    print("所有人的名片信息如下：")
    for name, info in business_cards.items():
        print(f"姓名: {name}")
        print(f"职位: {info['职位']}")
        print(f"住址: {info['住址']}")
        print()  # 打印一个空行分隔不同的名片信息
# 主程序
while True:
    print("""  
    请选择操作：  
    1. 添加名片信息  
    2. 查找名片信息  
    3. 列出所有人的名片信息  
    q. 退出系统  
    """)
    score = input("请输入选项（1/2/3/q）: ")
    if score.lower() == 'q':
        break
    elif score == '1':
        add_contact_info()
    elif score == '2':
        find_contact_info()
    elif score == '3':
        list_all_contacts()
    else:
        print("无效的选项，请重新输入。")