import time
import unittest
from ..basetoolclass import Base_geturl
from selenium.webdriver.common.by import By
class Login(Base_geturl):
        botton_page = (By.XPATH, '//*[@id="tab-outside"]')#切换至外部登录
        chongxinlogin=(By.ID,'tab-outside')#"切换外部登录"
        nameinout = (By.XPATH, '//*[@placeholder="请输入用户名称"]')
        pswinupt = (By.XPATH, '//*[@placeholder="请输入登录密码"]')
        login = (By.CSS_SELECTOR, '#pane-outside > form > div:nth-child(4) > div > button > span')
        # usernames = "wanghuimin"
        # userpaw = "Jinmaomj@2023"
        assert_login = (By.XPATH,'//*[text()="用户名或密码错误"]')#弹窗提示"用户名或密码错误"
        home_button=(By.ID,'tab-home')#首页按钮
        def Login_fram(self):
            """测试环境不判断"""
            if self.Wait_element(self.chongxinlogin):#如果出现是重新登录界面则进入判断
                self.click(self.chongxinlogin)#重新登陆按钮
                self.click(self.botton_page)#切换至外部登录
                return print("重新登录tab切换外部登录tab成功")
            if self.Wait_element(self.botton_page):
                self.click(self.botton_page)
        def Login_fram_DEV(self):
            """测试环境不判断"""
            self.Wait_element(self.chongxinlogin).click()
            self.info_log("切换外部登录")
        def input_account(self,usernames,pasward):
            self.send_keys(self.nameinout,usernames)
            self.info_log("输入用户名{}".format(usernames))
            self.send_keys(self.pswinupt, pasward)
            self.info_log("输入密码{}".format(pasward))
            self.click(self.login)
        def login_case(self,usernames,pasward):
            """登录账号密码验证"""
            self.max_windos()#最大化窗口
            self.getLogger().info("最大化窗口")
            self.Login_fram_DEV()
            self.input_account(usernames,pasward)#输入用户名密码
            return self.ele_dispaly(self.home_button)



