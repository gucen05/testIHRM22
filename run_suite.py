
# 1 创建测试套件
import time
import unittest
import HTMLTestRunner_PY3
import app
from script.temp_emp_params import TestEmployeeParams
from script.test_login_params import TestLoginParams

suite = unittest.TestSuite()
# 2 添加测试用例
suite.addTest(unittest.makeSuite(TestLoginParams))
suite.addTest(unittest.makeSuite(TestEmployeeParams))
# 3 定义测试报告名称
# ihrm_report = app.BASE_DIR + "/report/ihrm{}.html".format(time.strftime('%Y%m%d %H%M%S'))
ihrm_report = app.BASE_DIR + "/report/ihrm.html"
# 4 使用HTMLTestRunner_PY3生成测试报告
with open(ihrm_report, mode='wb') as f:
    # 实例化runner
    runner = HTMLTestRunner_PY3.HTMLTestRunner(f,verbosity=2, title="ihrm测试报告", description="这是个稍微美观一点儿的测试报告")
    # 使用runner运行测试套件，生成测试报告
    runner.run(suite)