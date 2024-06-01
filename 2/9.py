'''
准备工作：
        完成requests请求库： pip install requests

    导入requests
    import reqiests
用代码获取百度的内容

步骤：
    1、准备好百度的地址:https://ww.baidu.com
    2、发送请求
    requests.get(url='请求地址')
    3、获取返回的结果
    response = requests.get(url='https://www.baidu.com')
    4、返回打印的内容
    print(response.text)

'''
import requests

url = 'https://ww.baidu.com'

response = requests.get(url=url)

print(response.text)