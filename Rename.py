__author__ = '张伟伟'
# 重命名接口测试
import urllib.request
import json
import urllib
import urllib.parse
class Rename:
    baseUrl = "http://192.168.188.1:8080/smarthome/index.php/cloud/Rename/fileRename"
    isResult = None
    header = {
        "Accept-Language": "zh-Hans-CN, en-us",
        "Cookie": "PHPSESSID=l3ebqsm685ajadaqmb3jbajh74",
        " User - Agent": "SmartHome / 1 CFNetwork / 758.2.8 Darwin / 15.0.0",
        "Content - Type": "application / x - www - form - urlencoded;charset = utf - 8"
    }
    #重命名接口测试
    def testRename(self, sourcePath, targetPath):
        datett = {
            'targetPath': targetPath,
            'sourcePath': sourcePath,
            'token':0
        }
        dater = urllib.parse.urlencode(datett).encode("utf-8")
        respone = urllib.request.Request(self.baseUrl, dater, self.header)
        r = urllib.request.urlopen(respone)
        conn = r.read()
        conn = conn.decode()
        t = json.loads(conn)
        parmsCode = t.get("code")
        parmsMsg = t.get("msg")
        print("code:" + str(parmsCode) + "    "+ "msg:" + str(parmsMsg))
        # print(t.get("code"))
        # 获取code状态码
        # parms = t.get("code")
        # print("code:" + str(parms))
        # #获取文件名
        # # parms = t.get("list")
        # # for parm in parms:
        # #     fileName = parm.get("file_name")
        # #     print(fileName)
