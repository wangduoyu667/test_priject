import datetime
import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from basetoolclass import Base_geturl
from dev2.pageobject.test_page1_login import Login
from dev2.pageobject.test_page2_creat_cost import Creat_cb
from dev2.report.HTMLTestRunner import HTMLTestRunner
from ddt import file_data , ddt
@ddt
class Test_suit(unittest.TestCase,Login,Creat_cb):
    def setUp(self) -> None:
        print("开始运行用例")
        url='http://172.17.19.64:30010/login'
        #url = "http://10.160.152.222/home"
        path = Service('D:\case_tool\chromedriver.exe')#驱动绝对位置
        self.driver = webdriver.Chrome(service=path)#加载驱动
        self.driver.get(url)
        print("打开浏览器")
        Base_geturl(self.driver)#传递参数给基类
    def tearDown(self) -> None:
        time.sleep(3)
        self.driver.quit()
        print("用例运行结束")
    def test_01(self):
        self.creat_cost()
    # @file_data('./config/config.yaml')
    # def test_02(self,usernames,pasward):
    #     self.assertTrue(self.login_case(usernames,pasward), True)
if __name__ == '__main__':
    now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    current_dir = os.path.dirname(os.path.abspath(__file__))
    report_path = os.path.join(current_dir, "report", "report2" + now + ".html")
    discover=unittest.defaultTestLoader.discover(current_dir,"testsuit.py")#加载所有.py的文件用例
    with open(report_path, "wb") as report_file:
        runner = HTMLTestRunner(stream=report_file, title="Test Report", description="Test Results")
        runner.run(discover)