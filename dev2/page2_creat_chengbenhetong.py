import time
from basetoolclass import Base_geturl
from selenium.webdriver.common.by import By
class Login(Base_geturl):
        botton_page = (By.XPATH, '//*[@id="tab-outside"]')
        chongxinlogin=(By.XPATH,'//*[@id="app"]/div/div/div/div[2]/button/span')
        nameinout = (By.XPATH, '//*[@placeholder="请输入用户名称"]')
        pswinupt = (By.XPATH, '//*[@placeholder="请输入登录密码"]')
        login = (By.CSS_SELECTOR, '#pane-outside > form > div:nth-child(4) > div > button > span')
        usernames = "wanghuimin"
        userpaw = "Jinmaomj@2023"
        assert_login = (
        By.CSS_SELECTOR, '#app > div > div > div.main-page-body.flex-col.flex1.of-h > div.navbar.main-page-he'
                         'ader > div.navbar-top > div.navbar-right > div > button.el-button.el-button--primary.el-button--small > span')
        login_equal1=(By.XPATH,'/html/body/div[2]/p')
        def Login_fram(self):
            if self.Wait_element(self.chongxinlogin):#如果出现是重新登录界面则进入判断
                self.click(self.chongxinlogin)
                self.click(self.botton_page)
            else:self.click(self.botton_page)
        def username(self):
            self.send_keys(self.nameinout,self.usernames)
        def userpassward(self):
            self.send_keys(self.pswinupt,self.userpaw)
        def login_button(self):
            self.click(self.login)
        def login_assert(self):
             return self.Wait_element(self.assert_login).text
        def login_case(self):
            self.max_windos()#最大化窗口
            self.Login_fram()#切换登录界面
            self.username()#输入账号
            self.userpassward()#输入密码
            self.login_button()#登录
            print("输入账号{}，密码{}，点击登录".format(self.usernames,self.userpaw))
            self.assertequal(self.login_equal1)
