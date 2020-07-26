# 定义一个封装通用断言的函数
import json

import app


def assert_common_util(abc, response, status_code, success, code, message):
    abc.assertEqual(status_code, response.status_code) # 断言响应状态码
    abc.assertEqual(success, response.json().get("success"))  # 断言success
    abc.assertEqual(code, response.json().get("code"))  # 断言code
    abc.assertIn(message, response.json().get("message"))  # 断言message

# 定义一个读取外部数据文件的函数
def read_login_data(filename):
    """
    :param filename: 是一个数据文件的路径，应该要传我们login.json数据文件
    :return:
    """
    with open(filename,mode='r',encoding='utf-8') as f:
        jsonData = json.load(f)
        print(jsonData)
        # 把读取出来的json数据转换为列表元组形式
        # 定义个空列表，接收登录的数据
        temp_list = list()
        for login_data in jsonData:
            # print("login_data.values())", login_data.values())
            temp_list.append(tuple(login_data.values()))

    print("temp_list的值：", temp_list)
    return temp_list

# read_login_data("C:\\Users\\Ghost\\PycharmProjects\\testIHRM22\\data\\login.json")

def read_emp_data(filename, type):
    """
    :param filename:外部传入的员工模块的数据路径
    :param type: 是指员工的接口名（add_emp,query_emp,modify_emp,delete_emp）
    :return:
    """
    with open(filename,mode='r', encoding='utf-8') as f:
        jsonData = json.load(f) # 把数据文件加载成json格式
        print("加载的员工数据为：", jsonData)
        emp_data = jsonData.get(type) # 读取某个员工接口的数据(type是add_emp是时添加员工）
        print("emp_data为：", emp_data)
        # 把加载数来的员工数据，转换为列表元组形式
        temp_list = list() #定义空列表
        print("emp_data.values():", emp_data.values())
        temp_list.append(tuple(emp_data.values())) # 把读取出来的员工数据转化成列表元组对象
    print("读取员工数据为：", temp_list)
    return temp_list


# read_emp_data(app.BASE_DIR+"/data/employee.json","add_emp")

# read_emp_data(app.BASE_DIR+"/data/employee.json","query_emp")