# -*- coding: utf-8 -*-
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class EmailManager:
    def get_latest_html_file(self):
        directorys=r'C:\Users\86151\PycharmProjects\test_priject\dev2\report'
        html_files = [file for file in os.listdir(directorys) if file.endswith('.html')]
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

    def send_emails(self, paths=r'C:\Users\86151\PycharmProjects\test_priject\dev2\report\report220230817095856.html'):
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
        # 将HTML文件作为附件添加到邮件中
        with open(paths, 'rb') as file:
            fujian = MIMEText(file.read(), 'html', 'utf-8')
            fujian.add_header('Content-Disposition', 'attachment', filename=os.path.basename(paths))
            message.attach(fujian)
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
