from datetime import datetime
from selenium.webdriver.common.action_chains import ActionChains
from ..basetoolclass import Base_geturl
from selenium.webdriver.common.by import By
import unittest
class Creat_cb(Base_geturl):
        current_date = datetime.now().date()
        formatted_date = current_date.strftime("%Y-%m-%d")
        usernames='wanghuimin'
        pasward='123456'
        Attachments = r'C:\Users\86151\PycharmProjects\test_priject\dev2\config\cs.doc'
        chongxinlogin=(By.ID,'tab-outside')#"切换外部登录"
        nameinout = (By.XPATH, '//*[@placeholder="请输入用户名称"]')
        pswinupt = (By.XPATH, '//*[@placeholder="请输入登录密码"]')
        cost_text=(By.XPATH,'//*[text()="成本合同管理"]')#成本合同
        tes=(By.XPATH,'//*[@id="app"]/div/div/div[1]/div/div/div/ul/div[8]/li/div/i[2]')#成本合同下拉框
        new_cost=(By.XPATH,"//*[text()='创建供方采购合同']")#创建供方采购合同按钮

        contract_name=(By.XPATH,'//*[@placeholder="请输入合同名称"]')#采购合同脚本测试
        selece_date=(By.XPATH,'//*[@placeholder="选择开始日期"]')
        selece_date2 = (By.XPATH, '//*[@placeholder="选择结束日期"]')
        click_body=(By.XPATH,'//*[@id="app"]/div/div/div[2]/div[1]/div[1]')
        template_type=(By.XPATH,'//*[@class="el-radio__inner"][1]')
        input_code=(By.XPATH,'//*[@placeholder="请输入线下合同编号"]')
        #上传文件
        click_file_button=(By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div/di'
                                    'v/div[1]/div[1]/form/div[7]/div/div/div/div/div/div/button')
        click_file_button2=(By.XPATH,'//*[text()="选择附件"]')
        click_file_button3=(By.S,"body > div.el-dialog__wrapper > div > div.el-dialog__body > div > form > div > div.button-view.el-col.el-col-24 > div > div > div > button.el-button.el-button--primary.el-button--small")
        click_file_button4=(By.XPATH,'/html/body/div[3]/div/div[3]/span/button[2]/span')
        def click_cost_list(self):
            """进入成本合同列表"""
            self.no_selcet(self.tes,self.cost_text)
        def Login_fram_DEV(self):
            """测试环境不判断"""
            self.Wait_element(self.chongxinlogin).click()
            self.info_log("切换外部登录")
        def input_account(self,usernames,pasward):
            self.Wait_element(self.nameinout).send_keys(usernames)
            self.Wait_element(self.pswinupt).send_keys(pasward)
        def login_in(self):
            """获取token、进入首页"""
            self.max_windos()#最大化窗口
            self.Login_fram_DEV()
            self.input_account(self.usernames,self.pasward)#输入用户名密码
        def inputfile(self):
            # self.click(self.click_file_button)
            # self.click(self.click_file_button2)
            self.pywinautos(self.click_file_button,self.click_file_button2,self.click_file_button3,self.click_file_button4,self.Attachments)
        def creat_cost(self):
            self.login_in()
            self.click_cost_list()
            self.click(self.new_cost)
            self.send_keys(self.contract_name,self.formatted_date+'{}'.format(self.formatted_date))
            self.send_keys(self.selece_date,self.formatted_date)
            self.send_keys(self.selece_date2, self.formatted_date)
            self.click(self.click_body)
            self.inputfile()
            # self.send_keys(self.input_code,value="{}".format(self.formatted_date))
            # self.input_Attachments(self.update_Attachments)




