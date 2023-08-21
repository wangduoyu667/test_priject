# -*- coding: utf-8 -*-
import base64
import os
import smtplib
from datetime import time
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dev2.report.HTMLTestRunner import HTMLTestRunner
from Lib import HTMLTestRunner
import zipfile
class EmailManager:
    def __init__(self):
        self.result = HTMLTestRunner.TestResult()

    def capture_screenshot(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                # 捕获异常并保存错误截图
                path = r'C:\Users\86151\PycharmProjects\test_priject\dev2\report\images'
                # 生成时间戳
                timestrmap = time.strftime('%Y%m%d_%H.%M.%S')
                # 拼接文件路径
                imgPath = os.path.join(path, '%s.png' % str(timestrmap))
                screenshot_path = r"C:\Users\86151\PycharmProjects\test_priject\dev2\screenshot/screenshot.png"
                args[0].driver.save_screenshot(imgPath)
                # 将错误截图编码为Base64字符串
                with open(screenshot_path, "rb") as image_file:
                    encoded_image = base64.b64encode(image_file.read()).decode("utf-8")
                # 将Base64编码的图像字符串存储到全局变量中
                args[0].error_screenshot = encoded_image
                raise
        return wrapper
    def get_latest_html_file(self,configs=True):

        if  configs:
            directorys=r'C:\Users\86151\PycharmProjects\test_priject\dev2\report'
            html_files = [file for file in os.listdir(directorys) if file.endswith('.html')]
            if html_files:
                latest_html = max(html_files, key=lambda x: os.path.getmtime(os.path.join(directorys, x)))
                html_path = os.path.join(directorys, latest_html)
                print(html_path)
                return html_path
            return None
        else:
            directorys = r'C:\Users\86151\PycharmProjects\test_priject\dev2\report'
            html_files = [file for file in os.listdir(directorys) if file.endswith('.zip')]
            if html_files:
                latest_html = max(html_files, key=lambda x: os.path.getmtime(os.path.join(directorys, x)))
                html_path = os.path.join(directorys, latest_html)
                print(html_path)
                return html_path
            return None
        # 如果不存在HTML文件，则返回空值或抛出异常，根据您的需求进行处理
    # def send_email(self,paths=r'C:\Users\86151\PycharmProjects\test_priject\dev2\report\report220230817095856.html'):
    #     # now = time.strftime("%Y-%m-%d %H-%M", time.localtime())
    #     # 定义SMTP服务器
    #     smtpserver = 'smtp.qq.com'
    #     # 发送邮件的用户名和客户端密码(就是授权密码)
    #     username = '1207413125@qq.com'
    #     passwd = 'unrxlhmtuehehiab'  # 授权密码
    #     # 接收邮件的邮箱
    #     receiver = '1207413125@qq.com'
    #     # 创建邮件对象
    #     message = MIMEMultipart('related')
    #     # 邮件主题
    #     subject = '美居系统自动化测试报告'
    #     #paths = r'C:\Users\86151\PycharmProjects\test_priject\dev2\report\report220230817095856.html'
    #     fujian = MIMEText(open(paths, 'rb').read(), 'html', 'utf-8')
    #     # 把邮件的信息组装到邮件对象里面
    #     message['from'] = username
    #     message['to'] = receiver
    #     message['subject'] = subject
    #     message.attach(fujian)
    #     # 登录smtp服务器并发送邮件
    #     smtp = smtplib.SMTP()
    #     smtp.connect(smtpserver)
    #     smtp.login(username, passwd)
    #     smtp.sendmail(username, receiver, message.as_string())
    #     smtp.quit()

    def send_emails(self, paths):
        # now = time.strftime("%Y-%m-%d %H-%M", time.localtime())
        # 定义SMTP服务器
        smtpserver = 'smtp.qq.com'
        # 发送邮件的用户名和客户端密码(就是授权密码)
        username = '1207413125@qq.com'
        passwd = 'unrxlhmtuehehiab'  # 授权密码
        # 接收邮件的邮箱
        receiver = '1207413125@qq.com'
        # 创建邮件对象
        message = MIMEMultipart('related')
        # 邮件主题
        subject = '美居系统自动化测试报告'
        with open(paths, 'rb') as file:
            fujian = MIMEApplication(file.read())
            fujian.add_header('Content-Disposition', 'attachment', filename=os.path.basename(paths))
            message.attach(fujian)
        # 将HTML文件作为附件添加到邮件中
        # with open(paths, 'rb') as file:
        #     fujian = MIMEText(file.read(), 'html', 'utf-8')
        #     fujian.add_header('Content-Disposition', 'attachment', filename=os.path.basename(paths))
        #     message.attach(fujian)
        # 把邮件的信息组装到邮件对象里面
        message['from'] = username
        message['to'] = receiver
        message['subject'] = subject
        # 登录smtp服务器并发送邮件
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)
        smtp.login(username, passwd)
        smtp.sendmail(username, receiver, message.as_string())
        smtp.quit()
    def create_zip_file(self):
        zip_path = r'C:\Users\86151\PycharmProjects\test_priject\dev2\report\archive.zip'
        directory_path = r'C:\Users\86151\PycharmProjects\test_priject\dev2\report\images'
        with zipfile.ZipFile(zip_path, 'w') as zip_file:
            # 添加HTML文件到压缩包
            zip_file.write(self.get_latest_html_file(), os.path.basename(self.get_latest_html_file()))

            # 添加指定文件夹中的所有文件到压缩包
            for root, dirs, files in os.walk(directory_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    zip_file.write(file_path, os.path.relpath(file_path, directory_path))

# # 示例用法
# html_path = r'C:\Users\86151\PycharmProjects\test_priject\dev2\report\report220230817095856.html'
# directory_path = r'C:\Users\86151\PycharmProjects\test_priject\dev2\report'
# zip_path = r'C:\Users\86151\PycharmProjects\test_priject\dev2\report\archive.zip'
#
# my_object.create_zip_file(html_path, directory_path, zip_path)

