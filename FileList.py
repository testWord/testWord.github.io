__author__ = '张伟伟'
import urllib.request
import json
import urllib
import urllib.parse
class FileTest:
    baseUrl = "http://192.168.188.1:8080/smarthome/index.php/cloud/List/fileList"
    isResult = None
    header = {
        "Accept-Language": "zh-Hans-CN, en-us",
        "Cookie": "PHPSESSID=l3ebqsm685ajadaqmb3jbajh74",
        " User - Agent": "SmartHome / 1 CFNetwork / 758.2.8 Darwin / 15.0.0",
        "Content - Type": "application / x - www - form - urlencoded;charset = utf - 8"
    }
    # 登录接口方法测试测试
    def testMap(self,filePath,pageIndex,pageNum,sort,sortMode,type):

        datett = {
                  'filePath': filePath,
                  'pageIndex': pageIndex,
                  'pageNum': pageNum,
                  'sort': sort,
                  'sortMode': sortMode,
                  'token': 123,
                  'type': type
                 }
        dater = urllib.parse.urlencode(datett).encode("utf-8")
        respone = urllib.request.Request(self.baseUrl, dater, self.header)
        r = urllib.request.urlopen(respone)
        conn = r.read()
        conn = conn.decode()
        t = json.loads(conn)
        # print(t)
        parms = t.get("code")

        print("code:" + str(parms))
        # for parm in parms:
        #
        #     fileName = parm.get("file_name")
        #     print(fileName)




