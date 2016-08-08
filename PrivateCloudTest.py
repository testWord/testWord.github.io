import time
import urllib.request
import json
import urllib
import urllib.parse
from ExcelTest import ExlWrit


class PrivateCloudTest:
    baseUrl = "http://192.168.188.1:8080/smarthome/app/"
    isResult = None
    header = {
        "Accept-Language": "zh-Hans-CN, en-us",
        "Cookie": "PHPSESSID=u71cq242a2n3p79p0igsakagc6",
        " User - Agent": "SmartHome / 1 CFNetwork / 758.2.8 Darwin / 15.0.0",
        "Content - Type": "application / x - www - form - urlencoded;charset = utf - 8"
    }
    isFileName = True

    # 登录接口方法测试测试
    def testLogin(self, uname, upasswd):
        utime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        login = "login.php"
        url = self.baseUrl + login
        datett = {'uname': uname,
                  'upasswd': upasswd,
                  'utime': utime
                 }
        dater = urllib.parse.urlencode(datett).encode("utf-8")
        respone = urllib.request.urlopen(url=url, data=dater)
        conn = respone.read()
        conn = conn.decode()
        t = json.loads(conn)
        # print(conn)

        resultKey = t.get("result")
        if resultKey == 1:
            self.isResult = True
        else:
            self.isResult = False
        if self.isResult:
            print("登录接口测试通过")
            ExlWrit(0,"登录接口测试通过")
        else:
            print("登录接口测试失败")
            ExlWrit(0,"登录接口测试失败")

    # 获取mac地址测试
    def Status(self):
        respone = urllib.request.urlopen(url="http://192.168.188.1:8080/smarthome/app/checkshowstatus.php")
        conn = respone.read()
        conn = conn.decode()
        t = json.loads(conn)
        # print(conn)
        if t.get("mac") == "CO30412205R0000105":
            print("获取Mac测试通过")
            ExlWrit(1, "获取Mac测试通过")
        else:
            print("获取Mac测试不通过")
            ExlWrit(1, "获取Mac测试不通过")

    # 注销登录
    def OutAdmin(self,session_id,uname):
        datet = {'uname': uname,
                  'session_id': 1
              }
        dater = urllib.parse.urlencode(datet).encode("utf-8")
        respone = urllib.request.Request("http://192.168.188.1:8080/smarthome/app/Applogout.php", dater,self.header)
        r = urllib.request.urlopen(respone)
        conn = r.read()
        conn = conn.decode()
        t = json.loads(conn)
        if t.get("msg") == "注销成功":
            print("注销成功测试通过")
            ExlWrit(2, "注销成功测试通过")
        else:
            print("注销成功不通过")
            ExlWrit(2, "注销成功不通过")

    # 获取私有云文件名测试
    def Path1(self,uname,upasswd):
        fetchFile = "fetchFile.php"
        url = self.baseUrl + fetchFile
        datett = {'uname': uname,
                  'upasswd': upasswd
        }
        dater = urllib.parse.urlencode(datett).encode("utf-8")
        respone = urllib.request.Request(url, dater, self.header)
        r = urllib.request.urlopen(respone)
        conn = r.read()
        conn = conn.decode()
        t = json.loads(conn)

        # 打印字符串、获取文件名（fileName是否==root、public、camera、share）
        # print(t)
        # parm = t.get("result")
        # print(type(parm))
        # for i in parm:
        #     # print(type(i))
        #     print(i.get("fileName"))
        parm1 = t.get("value")
        if parm1 == 1:
            print("文件名获取测试通过")
            ExlWrit(3, "文件名获取测试通过")
        else:
            print("文件名获取不通过")
            ExlWrit(3, "文件名获取不通过")

    #文件上传方法接口测试



