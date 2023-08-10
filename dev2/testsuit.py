import datetime
import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from basetoolclass import Base_geturl
from dev2.pageobject.test_page1_login import Login
from dev2.report.HTMLTestRunner import HTMLTestRunner
from ddt import file_data , ddt
@ddt
class Test_suit(unittest.TestCase,Login):
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
        time.sleep(1)
        self.driver.quit()
        print("用例运行结束")
    @file_data('./config/config.yaml')
    def test_02(self,usernames,pasward):
        # self.login_case(usernames,pasward)
        # self.assertTrue(self.ele_dispaly(self.home_button),True)
        self.assertTrue(self.login_case(usernames,pasward), True)
if __name__ == '__main__':
    now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    current_dir = os.path.dirname(os.path.abspath(__file__))
    report_path = os.path.join(current_dir, "report", "report2" + now + ".html")
    # now = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")#获取当前时间
    discover=unittest.defaultTestLoader.discover(".")#加载所有.py的文件用例
    with open(report_path, "wb") as report_file:
        runner = HTMLTestRunner(stream=report_file, title="Test Report", description="Test Results")
        runner.run(discover)
    # Htmlfile = r"C:\Users\86151\PycharmProjects\pythonProject10\dev2\report\report2"+now+".html"#报告路径
    # f=open(Htmlfile,'wb')#打开二进制文件
    # runner=HTMLTestRunner.HTMLTestRunner(stream=f,title='美居测试报告',verbosity=1,description='详细测试用例结果')
    # runner.run(discover)
    # f.close()
