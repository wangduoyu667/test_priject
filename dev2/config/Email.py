# -*- coding: utf-8 -*-
import os
import smtplib
from datetime import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class EmailManager:
    def get_path(self):
        directory = r'C:\Users\86151\PycharmProjects\test_priject\dev2\report'  # 指定目录的路径
        html_files = [file for file in os.listdir(directory) if os.path.splitext(file)[1] == '.html']
        latest_html = max(html_files, key=os.path.getctime)
        html_path = os.path.join(directory, latest_html)
        print(html_path)
    def send_email(self):
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
        paths = r'C:\Users\86151\PycharmProjects\test_priject\dev2\report\report220230817095856.html'
        fujian = MIMEText(open(paths, 'rb').read(), 'html', 'utf-8')
        # 把邮件的信息组装到邮件对象里面
        message['from'] = username
        message['to'] = receiver
        message['subject'] = subject
        message.attach(fujian)
        # 登录smtp服务器并发送邮件
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)
        smtp.login(username, passwd)
        smtp.sendmail(username, receiver, message.as_string())
        smtp.quit()