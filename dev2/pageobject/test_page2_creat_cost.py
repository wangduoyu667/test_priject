from datetime import datetime
import time
from ..basetoolclass import Base_geturl
from selenium.webdriver.common.by import By
class Creat_cb(Base_geturl):
        current_date = datetime.now().date()
        formatted_date = current_date.strftime("%Y-%m-%d")
        usernames='wanghuimin'
        pasward='123456'
        Attachments = r'C:\Users\86151\PycharmProjects\test_priject\dev2\cs.doc'
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
        update_Attachments=(By.XPATH,'/html/body/div[2]/div/div[2]/div/form/div/div[1]/div/div/div/input')
        click_file_button3=(By.CSS_SELECTOR,"body > div.el-dialog__wrapper > div > div.el-dialog__body > div > form > div > div.button-view.el-col.el-col-24 > div > div > div > button.el-button.el-button--primary.el-button--small")
        click_file_button4=(By.CSS_SELECTOR,'body > div.el-dialog__wrapper > div > div.el-dialog__footer > span > button.el-button.el-button--primary.el-button--small > span')
        asert_input_file=(By.XPATH,"//*[text()='删除']")
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
            self.click_cost_list()
            self.click(self.new_cost)
        def base_config(self):
            """输入合同名称"""
            self.send_keys(self.contract_name,self.formatted_date+'{}'.format(self.formatted_date))
            """选择日期"""
            self.send_keys(self.selece_date,self.formatted_date)
            self.send_keys(self.selece_date2, self.formatted_date)
            self.click(self.click_body)
            """输入合同类型"""
            self.click(self.template_type)
        def creat_Subject(self):
            """创建我方合同主体"""
            button=(By.XPATH,'//*[text()="+添加合同主体"]')
            select_Subject=(By.XPATH,'//*[@placeholder="请选择主体类型"]')
            Subject_me=(By.XPATH,'//*[text()="我方公司"]')
            click_company=(By.XPATH,'//*[@placeholder="请选择公司名称"]')
            select_company=(By.XPATH,'//*[text()="北京物业长沙分公司"]')
            determine=(By.CSS_SELECTOR,'#app > div > div > div.main-page-body.flex-col.flex1.of-h > div.main-page-content.flex-row.flex1 > div > div > div.el-drawer__wrapper > div > div > section > div > div.footer-btn > button.el-button.el-button--primary.el-button--small > span')
            self.no_selcet(button,select_Subject)
            self.no_selcet(Subject_me, click_company)
            self.no_selcet(select_company, determine)
            # self.click2(select_company)
            #
            # self.click2(determine)
        def creat_Subject2(self):
            """创建对方合同主体"""
            button=(By.XPATH,'//*[text()="+添加合同主体"]')
            select_Subject=(By.XPATH,'//*[@placeholder="请选择主体类型"]')
            Subject_me=(By.XPATH,'//*[text()="对方公司"]')
            click_company=(By.XPATH,'//*[@placeholder="请选择公司名称"]')
            select_company=(By.XPATH,"//*[text()='长沙数据统计']")
            determine=(By.CSS_SELECTOR,'#app > div > div > div.main-page-body.flex-col.flex1.of-h > div.main-page-content.flex-row.flex1 > div > div > div.el-drawer__wrapper > div > div > section > div > div.footer-btn > button.el-button.el-button--primary.el-button--small > span')
            self.no_selcet(button, select_Subject)
            self.no_selcet(Subject_me, click_company)
            self.no_selcet(select_company, determine)
            # self.click2(select_company)
            # self.click2(determine)
        def inputfile(self):
            """定标附件上传用例"""
            # current_dir = os.path.dirname(os.path.abspath(__file__))
            # # 构建相对路径
            # file_path = os.path.join(current_dir, 'config', 'cs.doc')
            self.login_in()
            self.pywinautos(self.click_file_button,self.click_file_button2,self.Attachments)
            time.sleep(0.2)
            self.click(self.click_file_button3)
            a=self.ele_dispaly(self.asert_input_file)#获取删除按钮是否存在
            time.sleep(1)
            self.click(self.click_file_button4)
            return a
        def inputfile_contract(self):
            """合同附件上传用例"""
            click_file_button=(By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div/div/div[1]/div[1]/form/div[8]/div/div/div/div/div/div/button/span')
            click_file_button2=(By.CSS_SELECTOR,'body > div:nth-child(7) > div > div.el-dialog__body > div > form > div > div:nth-child(1) > div > div > div > div > button > span')
            click_file_button3=(By.CSS_SELECTOR,'body > div:nth-child(7) > div > div.el-dialog__body > div > form > div > div.button-view.el-col.el-col-24 > div > div > div > button.el-button.el-button--primary.el-button--small > span')
            click_file_button4=(By.CSS_SELECTOR,'body > div:nth-child(7) > div > div.el-dialog__footer > span > button.el-button.el-button--primary.el-button--small > span')
            self.pywinautos(click_file_button,click_file_button2,self.Attachments)
            time.sleep(0.2)
            self.click(click_file_button3)
            a=self.ele_dispaly(self.asert_input_file)#获取删除按钮是否存在
            time.sleep(1)
            self.click(click_file_button4)
            return a
        def inputfile_delete(self):
            """附件删除用例"""
            delete_logo=(By.XPATH,"//*[text()='删除成功']")
            delete_button=(By.XPATH,"//*[text()='删除']")
            delete_enter=(By.CSS_SELECTOR,'body > div.el-message-box__wrapper > div > div.el-message-box__btns > button.el-button.el-button--default.el-button--small.el-button--primary > span')
            self.login_in()
            self.pywinautos(self.click_file_button,self.click_file_button2,self.Attachments)#上传附件
            time.sleep(2)
            self.click(self.click_file_button3)#点击上传按钮
            self.click(delete_button)
            self.click(delete_enter)#确认删除
            return self.ele_dispaly(delete_logo)
        def creat_cost(self):
            """创建合同"""
            self.login_in()
            self.inputfile()#进入tab上传定标附件
            self.delay_time()
            self.inputfile_contract()
            self.base_config()  # 输入基本参数
            self.creat_Subject()
            self.creat_Subject2()
            self.delay_time()
            self.click_locxy(1190, 190)#拉动组件滚动条至底部



