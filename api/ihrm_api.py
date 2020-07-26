# 导包
import requests
import app
# from app import BASE_URL # 这种写法会导致一些潜在的问题
# 创建封装的类
class LoginApi:
    def __init__(self):
        self.login_url = app.BASE_URL + "/api/sys/login"

    def login(self, jsonData):
        print("获取到的登陆url为：", self.login_url)
        return requests.post(url=self.login_url,
                             json=jsonData,
                             headers=app.HEADERS)

# 创建封装员工模块的类
class EmployeeApi:
    def __init__(self):
        # 定义员工模块的URL
        self.emp_url = app.BASE_URL + "/api/sys/user"

    # 添加员工
    def add_emp(self, jsonData, out_headers):
        # 发送添加员工接口请求，并返回响应数据
        return requests.post(url=self.emp_url, json=jsonData, headers=out_headers)

    # 修改员工
    def modify_emp(self, emp_id, jsonData, out_headers):
        # 定义修改员工的URL
        modify_url = self.emp_url + "/" + emp_id
        # 发送修改员工请求
        return requests.put(url=modify_url, json=jsonData, headers=out_headers)

    # 查询员工
    def query_emp(self, emp_id, out_headers):
        # 定义查询员工的URL
        query_url = self.emp_url + "/" + emp_id
        # 发送查询员工请求
        return requests.get(url=query_url, headers=out_headers)

    # 删除员工
    def delete_emp(self,emp_id, out_headers):
        # 定义删除员工的URL
        delete_url = self.emp_url + "/" + emp_id
        # 发送删除员工请求
        return requests.delete(url=delete_url, headers=out_headers)