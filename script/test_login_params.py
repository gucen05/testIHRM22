
# 导入unittest
import unittest
# 创建unittest类
import app
from api.ihrm_api import LoginApi
from utils import assert_common_util, read_login_data
from parameterized import parameterized

class TestLoginParams(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 实例化api
        cls.login_api = LoginApi()

    login_file_path = app.BASE_DIR + "/data/login.json"

    @parameterized.expand(read_login_data(login_file_path))
    # 创建测试函数
    def test01_login(self,case_name, request_body, success, code, message, status_code):
        # 使用实例化的login_api发送登陆接口请求
        response = self.login_api.login(request_body)
        # 打印登陆的数据
        print(case_name)
        print("登陆结果为：", response.json())
        # 断言
        assert_common_util(self, response, status_code, success, code, message)
