

# 导包
import unittest
# 创建继承unittest.TestCase的测试类
from parameterized import parameterized

import app
from api.ihrm_api import LoginApi, EmployeeApi
from utils import assert_common_util, read_emp_data


class TestEmployeeParams(unittest.TestCase):

    # 实例化
    @classmethod
    def setUpClass(cls):
        # 实例化登陆模块的封装API
        cls.login_api = LoginApi()
        # 实例化员工模块
        cls.emp_api = EmployeeApi()

    # 实现员工的增删改查
    def test01_login(self):
        # 先调用登陆接口，并登陆成功
        response = self.login_api.login({"mobile":"13800000002",
                                         "password":"123456"})
        # 输出登陆的结果
        print("登陆的结果为：", response.json())
        # 把令牌保存并更新HEADERS中
        app.HEADERS["Authorization"] = "Bearer " + response.json().get("data")
        # 输出保存的app.HEADERS，查看结果
        print("更新之后的令牌为：", app.HEADERS)

    # 员工数据文件的路径
    emp_path = app.BASE_DIR + "/data/employee.json"

    @parameterized.expand(read_emp_data(emp_path, "add_emp"))
    def test02_add_emp(self,request_body, success,code,message,status_code):
        # 使用封装的添加员工接口添加员工
        response = self.emp_api.add_emp(request_body, app.HEADERS)
        # 打印添加的结果
        print("添加员工的结果为：", response.json())
        # 断言添加员工
        assert_common_util(self, response, status_code, success, code, message)
        # 提取员工ID，并把员工ID保存到全局变量
        app.EMP_ID = response.json().get("data").get("id")

    @parameterized.expand(read_emp_data(emp_path, "query_emp"))
    def test03_query_emp(self,success,code,message,status_code):
        # 调用封装的查询员工接口，并传给员工ID和请求头给查询员工接口
        response = self.emp_api.query_emp(app.EMP_ID, app.HEADERS)
        # 打印查询员工的结果
        print("查询员工的结果为：", response.json())
        # 断言
        assert_common_util(self, response, status_code, success, code, message)

    @parameterized.expand(read_emp_data(emp_path, "modify_emp"))
    def test04_modify_emp(self,request_body, success,code,message,status_code):
        # 调用修改员工接口，并传递请求体、员工id,请求头，实现修改员工
        response = self.emp_api.modify_emp(app.EMP_ID, request_body, app.HEADERS)
        # 打印修改员工的结果
        print("修改员工的结果", response.json())
        # 断言
        assert_common_util(self, response, status_code, success, code, message)

    @parameterized.expand(read_emp_data(emp_path, "delete_emp"))
    def test05_delete_emp(self,success,code,message,status_code):
        # 调用删除员工接口
        response = self.emp_api.delete_emp(app.EMP_ID, app.HEADERS)
        # 打印删除的结果
        print("删除的结果为：", response.json())
        # 断言
        assert_common_util(self, response, status_code, success, code, message)

