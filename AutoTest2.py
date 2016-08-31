__author__ = 'ThinkPad'
import os
import HTMLTestRunner
import unittest
from selenium import webdriver
import time

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4.2'
desired_caps['deviceName'] = 'aae85f3a'
desired_caps['appPackage'] = 'com.unicocloud.smarthome'
desired_caps['appActivity'] = 'com.unicocloud.smarthome.activity.LoginActivity'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
class elementA(unittest.TestCase):
    def test_ebudiu(self):
        driver.find_element_by_id("com.unicocloud.smarthome:id/searchImageButton").click()
        # e1 = driver.find_element_by_id("com.unicocloud.smarthome:id/ipEditText")
        # e1.send_keys("192.168.188.1")
        time.sleep(6)
        driver.find_element_by_id("android:id/text1").click()
        time.sleep(1)
        e2 = driver.find_element_by_id("com.unicocloud.smarthome:id/userEditText")
        e2.send_keys("admin")
        e3 = driver.find_element_by_id("com.unicocloud.smarthome:id/passwordEditText")
        e3.send_keys("admin")
        driver.find_element_by_id("com.unicocloud.smarthome:id/loginCheckBox").click()
        e4 = driver.find_element_by_id("com.unicocloud.smarthome:id/loginButton")
        e4.click()
        driver.find_element_by_id("com.unicocloud.smarthome:id/titleLeft").click()
        time.sleep(1)
        # driver.find_element_by_tag_name("注销").click()
        t = driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'注销')]").click()
        driver.find_element_by_id("android:id/button1").click()
if __name__ == '__main__':
    testunit = unittest.TestSuite()
    # 定义一个单元测试容器
    testunit.addTest(elementA("test_ebudiu"))
    # 将测试用例加入到测试容器中
    # testunit.addTest(elementA('test_a'))
    filename = "./myAppiumLog.html"
    # 定义个报告存放路径。
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Report_title',
                                           description='Report_description')  # 使用HTMLTestRunner配置参数，输出报告路径、报告标题、描述
    runner.run(testunit)
    # 自动进行测试