# 设置全局变量
import os
# 项目根URL
BASE_URL = "http://ihrm-test.itheima.net"
# 项目根目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# 请求头
# 后续每个接口都需要引用请求头，需要注意的是，其中的手动设置的令牌是会失效的，所以在代码运行过程当中
# 我们需要重新更新令牌
HEADERS = {"Content-Type":"application/json",
           "Authorization":"Bearer 59ae854f-82f2-427f-a0f4-b32685559610"}
# 员工ID
# 后续添加员工时，要保存的员工ID
EMP_ID = ""