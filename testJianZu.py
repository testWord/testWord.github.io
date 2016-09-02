__author__ = '张伟伟'
import urllib.request
import json
import urllib
import urllib.parse
class Jianzu:
    baseUrl = "http://jianzhugang.com:8080/projectHires/query"
    header = {
        "Accept-Language": "zh-Hans-CN, en-us",
        # " User - Agent": "Mozilla/5.0 (Linux; Android 5.0.2; X608 Build/ACXCNCM5501304131S) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36",
        "Content - Type": "application / x - www - form - urlencoded;charset = utf - 8"

    }
    def JianzuTest(self, page,size,status):
        datett = {
            'page': page,
            'size':size,
            'status':status,
        }
        dater = urllib.parse.urlencode(datett).encode("utf-8")
        respone = urllib.request.Request(self.baseUrl, dater, self.header)
        r = urllib.request.urlopen(respone)
        conn = r.read()
        conn = conn.decode()
        t = json.loads(conn)
        parmsCode = t.get("content")
        Number = t.get("totalElements")
        for i in range(0,Number):
            value1 = parmsCode[i].get("phone")
            value2 = parmsCode[i].get("publishedTime")
            value3 = parmsCode[i].get("project")
            value8 = parmsCode[i].get("type")
            value4 = value3.get("name")
            value5 = value3.get("displayAddress")
            value6 = value3.get("endTime")
            value7 = parmsCode[i].get("salary")
            value9 = value8.get("text")
            value11= parmsCode[i].get("teamNeeds")
            # for j in range(0,len(value11)):
            #     value12 = value11[j].get("teamType")
            #     value13 = value12.get("id")
            #     value14 = value12.get("title")
            if (value1==None):
                print("项目名称:" + " " + str(value4))
                print("项目地址:" + " " + str(value5))
                print("手机号:"+" "+str(parmsCode[i].get("contacts")))
                print("发布时间:" + " " + str(value2))
                print("招聘截止时间:" + " " + str(value6))
                for j in range(0, len(value11)):
                    value12 = value11[j].get("teamType")
                    value13 = value12.get("id")
                    value14 = value12.get("title")
                    print("所需人数:" + " " + str(value14) + ":" + "  " + str(value13)+"人")
                print("薪资/价格:" + " " + value7)
                print("类型:" + " " + value9)
                print("----------------------------------------")
            else:
                print("项目名称:" + " " + str(value4))
                print("项目地址:" + " " + str(value5))
                print("手机号:"+" "+str(value1))
                print("发布时间:" + " " + value2)
                print("招聘截止时间:" + " " + str(value6))
                for j in range(0, len(value11)):
                    value12 = value11[j].get("teamType")
                    value13 = value12.get("id")
                    value14 = value12.get("title")
                    print("所需人数:" + " " + str(value14) + ":" + "  " + str(value13) + "人")
                print("薪资/价格:" + " " + value7)
                print("类型:" + " " + value9)
                print("----------------------------------------")
    def totalElements(self, page,size,status):
        datett = {
            'page': page,
            'size': size,
            'status': status,
        }
        dater = urllib.parse.urlencode(datett).encode("utf-8")
        respone = urllib.request.Request(self.baseUrl, dater, self.header)
        r = urllib.request.urlopen(respone)
        conn = r.read()
        conn = conn.decode()
        t = json.loads(conn)
        Number = t.get("totalElements")
        return Number

if __name__ == '__main__':
    testJianzu1 =Jianzu()
    t =testJianzu1.totalElements(0,20,"AUDITED")
    testJianzu1.JianzuTest(0,t, "AUDITED")


