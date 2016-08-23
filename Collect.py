__author__ = '张伟伟'
# 文件收藏接口测试
import urllib.request
import json
import urllib
import urllib.parse
class Collect:
    baseUrl = "http://192.168.188.1:8080/smarthome/index.php/cloud/Collect/fileCollect"
    header = {
        "Accept-Language": "zh-Hans-CN, en-us",
        " User - Agent": "SmartHome / 1 CFNetwork / 758.2.8 Darwin / 15.0.0",
        "Content - Type": "application / x - www - form - urlencoded;charset = utf - 8"
    }
    #    文件收藏接口测试
    def CollectFile(self, filePath,type):
        datett = {
            'filePath': filePath,
            'type':type,
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
