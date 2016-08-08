__author__ = 'Zhangweiwei'
from PrivateCloudTest import PrivateCloudTest
class MainTest:

    # 测试登录接口
    tester = PrivateCloudTest()
    tester.testLogin('admin', 'admin')

    # 测试状态值及mac值是否正确
    tester.Status()

    # 测试应用注销测试
    # tester.OutAdmin("session_id","admin")

    # 测试文件名测试
    tester.Path1("admin","admin")



