
import time
import logging
import logging.handlers
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.support.select import Select #下拉框
import os
from pywinauto import Desktop
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
            self.screenshort()
            print("未找到元素{}".format(loc))
            return False
    def send_keys(self,loc,value=None):#等待元素并输入
        self.Wait_element(loc).send_keys(value)
    def click(self,loc):
        self.Wait_element(loc).click()
    def switch_window(self):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
    def max_windos(self):
        self.driver.maximize_window()
    def tishi(self,loc):
        if self.Wait_element(loc).text:
            return self.Wait_element(loc).text
    def selcet(self,loc,index=0):#下拉框方法
        value=self.find_element(loc)
        select_eles=Select(value)
        select_eles.select_by_index(index)#通过索引选择下拉元素
    def no_selcet(self,loc,loc2):#非下拉框方法
         self.click(loc)
         time.sleep(0.2)
         self.click(loc2)
         return print("获取下拉框元素")
    def input_file(self,loc,filepath):#传输上传附件inupt  XPTH
        print("上传附件{}中".format(filepath))
        self.find_element(loc).sendkeys(filepath)
        return print("上传{}完毕".format(filepath))
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
        return self.getLogger().info(msg)
    # def input_Attachments(self,loc,file):
    #     self.send_keys(loc,file)
    def input_files(self,loc,file):
        el = self.Wait_element(loc)
        self.driver.execute_script('arguments[0].style.visibility="visible"', el)
        el.send_keys(file)
    def pywinautos(self,button1,button2,file):
        self.click(button1)
        self.click(button2)
        app = Desktop()
        dialog = app['打开']  # 根据名字找到弹出窗口
        dialog["Edit"].type_keys(file)  # 在输入框中输入值
        time.sleep(2)
        dialog["打开(O)"].double_click()
        print("调用上传文件方法成功，上传附件成功")



