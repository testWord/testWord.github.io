__author__ = '张伟伟'
import urllib.request
import json
import urllib
import urllib.parse
class Jianzu:
    baseUrl = "http://jianzhugang.com:8080/teams/query"
    header = {
        "Accept-Language": "zh-Hans-CN, en-us",
            "Content - Type": "application / x - www - form - urlencoded;charset = utf - 8"

    }
    def JianzuTest(self, page,size,status,typeId):
        datett = {
            'page': page,
            'size':size,
            'status':status,
            "typeId":typeId
        }
        dater = urllib.parse.urlencode(datett).encode("utf-8")
        respone = urllib.request.Request(self.baseUrl, dater, self.header)
        r = urllib.request.urlopen(respone)
        conn = r.read()
        conn = conn.decode()
        t = json.loads(conn)
        parmsCode = t.get("content")

        for i in range(0,13882):
            value1 = parmsCode[i].get("title")
            value2 = parmsCode[i].get("teamType")
            value6 = value2.get("title")
            value3 = parmsCode[i].get("userName")
            value4 = parmsCode[i].get("starsLevel")
            value5 = parmsCode[i].get("displayAddress")
            print("班组负责人:" + " " + str(value1))
            print("班组类型:" + " " + str(value6))
            print("联系方式:"+" "+str(value3))
            print("星级:" + " " + str(value4))
            print("地址:" + " " + str(value5))
            print(i)
            print("----------------------------------------")

    def totalElements(self, page,size,status,typeId):
        datett = {
            'page': page,
            'size': size,
            'status': status,
            "typeId": typeId
        }
        dater = urllib.parse.urlencode(datett).encode("utf-8")
        respone = urllib.request.Request(self.baseUrl, dater, self.header)
        r = urllib.request.urlopen(respone)
        conn = r.read()
        conn = conn.decode()
        t = json.loads(conn)
        parmsCode = t.get("totalElements")
        return parmsCode


if __name__ == '__main__':
    testJianzu1 =Jianzu()
    t1 = testJianzu1.totalElements(0,20,"TEAM_STATUS_NORMAL",1)
    t2 = testJianzu1.totalElements(0,20,"TEAM_STATUS_NORMAL",2)
    t3 = testJianzu1.totalElements(0, 20, "TEAM_STATUS_NORMAL", 3)
    t4 = testJianzu1.totalElements(0, 20, "TEAM_STATUS_NORMAL", 4)
    t5 = testJianzu1.totalElements(0, 20, "TEAM_STATUS_NORMAL", 5)
    t6 = testJianzu1.totalElements(0, 20, "TEAM_STATUS_NORMAL", 6)
    t7 = testJianzu1.totalElements(0, 20, "TEAM_STATUS_NORMAL", 7)
    t8 = testJianzu1.totalElements(0, 20, "TEAM_STATUS_NORMAL", 8)
    t9 = testJianzu1.totalElements(0, 20, "TEAM_STATUS_NORMAL", 9)
    t10 = testJianzu1.totalElements(0, 20, "TEAM_STATUS_NORMAL", 10)
    t11 = testJianzu1.totalElements(0, 20, "TEAM_STATUS_NORMAL", 11)

    print(t1)
    print(t2)
    print(t3)
    print(t4)
    print(t5)
    print(t6)
    print(t7)



    # testJianzu1.JianzuTest(0,13882, "TEAM_STATUS_NORMAL",1)


