
# 导入unittest
import unittest
# 创建unittest类
from api.ihrm_api import LoginApi
from utils import assert_common_util

class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 实例化api
        cls.login_api = LoginApi()


    # 创建测试函数
    def test01_login_success(self):
        # 使用实例化的login_api发送登陆接口请求
        response = self.login_api.login({"mobile":"13800000002","password":"123456"})
        # 打印登陆的数据
        print("登陆成功的结果为：", response.json())
        # 断言
        assert_common_util(self, response, 200, True, 10000, "操作成功")

    # 手机号码未注册
    def test02_mobile_is_not_reigst(self):
        # 使用实例化的login_api发送登陆接口请求
        response = self.login_api.login({"mobile":"14000000002","password":"123456"})
        # 打印登陆的数据
        print("手机号码未注册的结果为：", response.json())
        # 断言
        assert_common_util(self, response, 200, False, 20001, "用户名或密码错误")

    # 手机号码长度超过11位
    def test03_mobile_length_greter_11(self):
        # 使用实例化的login_api发送登陆接口请求
        response = self.login_api.login({"mobile":"1400000000211","password":"123456"})
        # 打印登陆的数据
        print("手机号码长度超过11位的结果为：", response.json())
        # 断言
        assert_common_util(self, response, 200, False, 20001, "用户名或密码错误")

    # 手机号码长度小于11位
    def test04_mobile_length_less_11(self):
        # 使用实例化的login_api发送登陆接口请求
        response = self.login_api.login({"mobile":"1400000","password":"123456"})
        # 打印登陆的数据
        print("手机号码长度小于11位的结果为：", response.json())
        # 断言
        assert_common_util(self, response, 200, False, 20001, "用户名或密码错误")

    # 手机号码为空
    def test05_mobile_is_empty(self):
        # 使用实例化的login_api发送登陆接口请求
        response = self.login_api.login({"mobile": "", "password": "123456"})
        # 打印登陆的数据
        print("手机号码为空的结果为：", response.json())
        # 断言
        assert_common_util(self, response, 200, False, 20001, "用户名或密码错误")

    # 密码错误
    def test06_password_is_error(self):
        # 使用实例化的login_api发送登陆接口请求
        response = self.login_api.login({"mobile": "13800000002", "password": "error"})
        # 打印登陆的数据
        print("密码错误的结果为：", response.json())
        # 断言
        assert_common_util(self, response, 200, False, 20001, "用户名或密码错误")

    # 密码长度不够
    def test07_password_length_is_not_enough(self):
        # 使用实例化的login_api发送登陆接口请求
        response = self.login_api.login({"mobile": "13800000002", "password": "1"})
        # 打印登陆的数据
        print("密码错误的结果为：", response.json())
        # 断言
        assert_common_util(self, response, 200, False, 20001, "用户名或密码错误")

    # 密码中有特殊字符
    def test08_password_has_special_chars(self):
        # 使用实例化的login_api发送登陆接口请求
        response = self.login_api.login({"mobile": "13800000002", "password": "~!@#$%^&*()_+\\"})
        # 打印登陆的数据
        print("密码中有特殊字符的结果为：", response.json())
        # 断言
        assert_common_util(self, response, 200, False, 20001, "用户名或密码错误")

    # 少参-缺少mobile
    def test09_less_params_mobile(self):
        # 使用实例化的login_api发送登陆接口请求
        response = self.login_api.login({"password": "~!@#$%^&*()_+\\"})
        # 打印登陆的数据
        print("少参-缺少mobile:", response.json())
        # 断言
        assert_common_util(self, response, 200, False, 20001, "用户名或密码错误")

    # 少参-缺少password
    def test10_less_params_password(self):
        # 使用实例化的login_api发送登陆接口请求
        response = self.login_api.login({"mobile":"123123123"})
        # 打印登陆的数据
        print("少参-缺少password:", response.json())
        # 断言
        assert_common_util(self, response, 200, False, 20001, "用户名或密码错误")

    # 无参-传递{}
    def test11_none_params1(self):
        # 使用实例化的login_api发送登陆接口请求
        response = self.login_api.login({})
        # 打印登陆的数据
        print("无参-传递{}:", response.json())
        # 断言
        assert_common_util(self, response, 200, False, 20001, "用户名或密码错误")

    # 无参-传递null
    def test12_none_null(self):
        # 使用实例化的login_api发送登陆接口请求
        response = self.login_api.login(None)
        # 打印登陆的数据
        print("无参-传递null:", response.json())
        # 断言
        assert_common_util(self, response, 200, False, 99999, "抱歉，系统繁忙，请稍后重试")

    # 错误参数
    def test13_incorrect_params(self):
        # 使用实例化的login_api发送登陆接口请求
        response = self.login_api.login({"mboile":"13800000002", "password":"123456"})
        # 打印登陆的数据
        print("错误参数:", response.json())
        # 断言
        assert_common_util(self, response, 200, False, 20001, "用户名或密码错误")

    # 多参
    def test14_more_params(self):
        # 使用实例化的login_api发送登陆接口请求
        response = self.login_api.login({"mobile":"13800000002", "password":"123456", "more":"111"})
        # 打印登陆的数据
        print("错误参数:", response.json())
        # 断言
        assert_common_util(self, response, 200, True, 10000, "操作成功")

