import smtplib
import time
import logging
import logging.handlers
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.support.select import Select #下拉框
import os
from pywinauto import Desktop
from selenium.webdriver.common.action_chains import ActionChains
class Base_geturl:
    loggers = None
    def __init__(self,driver):
        loggers = None
        self.driver=driver
        self.imgPath=r'C:\Users\86151\PycharmProjects\pythonProject10\dev2\test_report'
    def find_element(self, loc):  # loc传入元组,原则包含定位类型、定位元素表达式
            return self.driver.find_element(*loc)
    def Wait_element(self,loc):#元素等待，返回元素
            self.getLogger().info("寻找等待定位元素{}".format(loc))
            return WebDriverWait(self.driver,3).until(Ec.visibility_of_element_located(loc))
    def ele_dispaly(self,loc):#判断是否找到元素,用作断言
        try:
            self.Wait_element(loc).is_displayed()
            self.info_log(msg="获取断言元素{}".format(loc))
            return True
        except:
            self.getImage()
            #self.screenshort()
            print("未找到元素{}".format(loc))
            return False
    def send_keys(self,loc,value=None):#等待元素并输入
        self.Wait_element(loc).send_keys(value)
    def click(self,loc):
        self.Wait_element(loc).click()
    def click2(self,loc):
        """等待出现，解决元素被遮挡"""
        a=ActionChains(self.driver)
        element = self.Wait_element(loc)
        a.move_to_element(element).perform()
        element.click()
        #self.Wait_element(loc).click()
    def switch_window(self):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
    def max_windos(self):
        self.driver.maximize_window()
    def selcet(self,loc,index=0):#下拉框方法
        value=self.find_element(loc)
        select_eles=Select(value)
        select_eles.select_by_index(index)#通过索引选择下拉元素
    def no_selcet(self,loc,loc2):#非下拉框方法
         self.click2(loc)
         self.delay_time()
         self.click2(loc2)
         return print("获取下拉框元素")
    # 截图
    def screenshort(self):
        '''
        截图方法
        :return:
        '''
        now = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
        self.driver.get_screenshot_as_file('screenshot/' + now + ".png")
        print('screenshot:', now, '.png')
        screenshot_path = os.path.abspath('screenshot/')
        print("截图路径:", screenshot_path)
        self.info_log(msg="截图路径:{},截图名称".format(screenshot_path)+now+'.png')
    def getLogger(self):
        # 2.创建日志器对象 / 设置日志级
        logger = logging.getLogger("root")
        logger.setLevel(level=logging.INFO)
        # 3.创建输出到控制台 / 文件
        ls = logging.StreamHandler()  # 按天分割，分割为5个
        # 判断log文件夹是否存在，不存在即创建
        path = "./logs"
        if not os.path.exists(path):
            os.mkdir(path)
        lf = logging.handlers.TimedRotatingFileHandler(filename=r"logs/test.log", when="D", backupCount=5)
        # 4.创建格式化器
        fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s] [line:%(lineno)d] - %(message)s'
        formatter = logging.Formatter(fmt=fmt)
        # 5.将格式化器添加到处理器
        ls.setFormatter(formatter)
        lf.setFormatter(formatter)
        # 6.添加处理器到日志器(添加判断：如果已经有处理器，就不需要再添加)
        if not logger.handlers:
            logger.addHandler(ls)
            logger.addHandler(lf)
        self.loggers = logger
        return self.loggers
    def info_log(self,msg="运行中"):
        #a=self.getLogger().info(msg)
        return self.getLogger().info(msg)
    def assert_ele(self,loc):
        self.info_log(msg="获取断言元素{}".format(loc))
        if self.find_element(loc):
            a=True
            return a
        else:a=False
        return a
    def input_Attachments(self,loc,file):
        self.send_keys(loc,file)
    # def input_Attachments(self,loc,file):
    #     self.send_keys(loc,file)
    def input_files(self,loc,file):
        el = self.Wait_element(loc)
        self.driver.execute_script('arguments[0].style.visibility="visible"', el)
        el.send_keys(file)
    # def pywinautos(self,button1,button2,file):
    #     '''
    #
    #     :param button1: 上传附件外部按钮
    #     :param button2: 上传附件组件内部按钮
    #     :param file:    上传附件地址
    #     :return:
    #     '''
    #     self.click(button1)
    #     time.sleep(1)
    #     self.click(button2)
    #     app = Desktop()
    #     dialog = app['打开']  # 根据名字找到弹出窗口
    #     dialog["Edit"].type_keys(file)  # 在输入框中输入值
    #     self.delay_time(5)
    #     dialog["打开(O)"].double_click()
    #     print("调用上传文件方法成功，上传附件成功")

    def pywinautos(self, button1, button2,file):
        '''

        :param button1: 上传附件外部按钮
        :param button2: 上传附件组件内部按钮
        :param file:    上传附件地址
        :return:
        '''
        self.click(button1)
        time.sleep(1)
        self.click(button2)
        app = Desktop()
        dialog = app['打开']  # 根据名字找到弹出窗口
        dialog["Edit"].type_keys(file)  # 在输入框中输入值
        self.delay_time(5)
        dialog["Edit"].type_keys("{ENTER}")  # 模拟按下Enter键
        print("调用上传文件方法成功，上传附件成功")
    def delay_time(self,times=0.2):
        self.driver.implicitly_wait(times)

    def click_locxys(self, element, x, y, left_click=False):
        '''
        element: 定位到的元素
        x: 相对于元素的x坐标
        y: 相对于元素的y坐标
        left_click: True为鼠标左键点击，否则为右键点击
        '''
        ActionChains(self.driver).move_to_element(self.Wait_element(element)).perform()  # 将鼠标移动到指定元素的位置
        if left_click:
            ActionChains(self.driver).move_by_offset(x, y).double_click().perform()
            self.screenshort()# 移动鼠标相对坐标并进行左键点击操作
        else:
            ActionChains(self.driver).move_by_offset(x, y).context_click().perform()
            self.screenshort()# 移动鼠标相对坐标并进行右键点击操作
    def getImage(self):
        '''
        截取图片,并保存在images文件夹
        :return: 无
        '''
        self.delay_time()
        path=r'C:\Users\86151\PycharmProjects\test_priject\dev2\report\images'
        # 生成时间戳
        timestrmap = time.strftime('%Y%m%d_%H.%M.%S')
        # 拼接文件路径
        imgPath = os.path.join(path, '%s.png' % str(timestrmap))
        # 使用WebDriver的save_screenshot方法截取屏幕截图并保存
        self.driver.save_screenshot(imgPath)
        # 打印截图文件名
        print('screenshot:', timestrmap, '.png')

    def send_email(self):
        # now = time.strftime("%Y-%m-%d %H-%M", time.localtime())
        #定义SMTP服务器
        smtpserver = 'smtp.qq.com'
        #发送邮件的用户名和客户端密码(就是授权密码)
        username = '1207413125@qq.com'
        passwd = 'unrxlhmtuehehiab' #授权密码
        #接收邮件的邮箱
        receiver = '1207413125@qq.com'
        #创建邮件对象
        message = MIMEMultipart('related')
        #邮件主题
        subject = '美居系统自动化测试报告'
        paths=r'C:\Users\86151\PycharmProjects\test_priject\dev2\report\.html'
        fujian = MIMEText(open(paths,'rb').read(),'html','utf-8')
        #把邮件的信息组装到邮件对象里面
        message['from']=username
        message['to']=receiver
        message['subject']=subject
        message.attach(fujian)
        #登录smtp服务器并发送邮件
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)
        smtp.login(username,passwd)
        smtp.sendmail(username,receiver,message.as_string())
        smtp.quit()




