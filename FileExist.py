__author__ = '张伟伟'
# 文件存在check接口测试
import urllib.request
import json
import urllib
import urllib.parse
class FileExist:
    baseUrl = "http://192.168.188.1:8080/smarthome/index.php/cloud/File/fileExist"
    header = {
        "Accept-Language": "zh-Hans-CN, en-us",
        " User - Agent": "SmartHome / 1 CFNetwork / 758.2.8 Darwin / 15.0.0",
        "Content - Type": "application / x - www - form - urlencoded;charset = utf - 8"
    }
    #  文件存在check接口测试
    def FileExistT(self, filePath):
        datett = {
            'filePath': filePath,
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
        parmsObj = t.get("obj")
        parmsObj1 = parmsObj.get("exist_flg")
        print("----------start----------")
        if parmsObj1=="1":

            print("code:" + str(parmsCode) + "    "+ "msg:" + str(parmsMsg)+"    "+"该文件存在并可以打开")

        elif parmsObj1=="0":
            print("code:" + str(parmsCode) + "    " + "msg:" + str(parmsMsg) + "    " + "该文件不存在并不可以打开")
        else:
            print("接口有问题！！！！！")
        print("----------end----------")

