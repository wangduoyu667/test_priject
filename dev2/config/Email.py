# -*- coding: utf-8 -*-
import os
import smtplib
import time
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import zipfile
from dev2.report import HTMLTestRunner
class EmailManager:
    def __init__(self):
        self.result = HTMLTestRunner.TestResult()
        self.directorys=r'C:\Users\86151\PycharmProjects\test_priject\dev2\report'
        self.path = r'C:\Users\86151\PycharmProjects\test_priject\dev2\report\images'
    def capture_screenshot(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                time.sleep(2)
                # 捕获异常并保存错误截图
                path = r'C:\Users\86151\PycharmProjects\test_priject\dev2\report\images'
                # 生成时间戳
                timestrmap = time.strftime('%Y%m%d_%H.%M.%S')
                # 拼接文件路径
                imgPath = os.path.join(path, '%s.png' % str(timestrmap))
                args[0].driver.save_screenshot(imgPath)
                print('screenshot:', timestrmap, '.png')
                raise
        return wrapper

    # def capture_screenshot(func):
    #     def wrapper(*args, **kwargs):
    #         try:
    #             return func(*args, **kwargs)
    #         except Exception as e:
    #             # 捕获异常并保存错误截图
    #             path = r'C:\Users\86151\PycharmProjects\test_priject\dev2\report\images'
    #             # 生成时间戳
    #             timestrmap = time.strftime('%Y%m%d_%H.%M.%S')
    #             # 拼接文件路径
    #             imgPath = os.path.join(path, '%s.png' % str(timestrmap))
    #             screenshot_path = r"C:\Users\86151\PycharmProjects\test_priject\dev2\screenshot/screenshot.png"
    #             args[0].driver.save_screenshot(imgPath)
    #             # 将错误截图编码为Base64字符串
    #             with open(screenshot_path, "rb") as image_file:
    #                 encoded_image = base64.b64encode(image_file.read()).decode("utf-8")
    #             # 将Base64编码的图像字符串存储到全局变量中
    #             args[0].error_screenshot = encoded_image
    #             raise
    #     return wrapper
    def get_latest_html_file(self,configs=True):
        if  configs==True:
            html_files = [file for file in os.listdir(self.directorys) if file.endswith('.html')]
            if html_files:
                latest_html = max(html_files, key=lambda x: os.path.getmtime(os.path.join(self.directorys, x)))
                html_path = os.path.join(self.directorys, latest_html)
                print(html_path)
                return html_path
            return None
        else:
            zip_files = [file for file in os.listdir(self.directorys) if file.endswith('.zip')]
            if zip_files:
                latest_zip = max(zip_files, key=lambda x: os.path.getmtime(os.path.join(self.directorys, x)))
                zip_path = os.path.join(self.directorys, latest_zip)
                print(zip_path)
                return zip_path
            return None
    # def send_emails(self, paths):
    #    try:
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
    #     with open(paths, 'rb') as file:
    #         fujian = MIMEApplication(file.read())
    #         fujian.add_header('Content-Disposition', 'attachment', filename=os.path.basename(paths))
    #         message.attach(fujian)
    #     message['from'] = username
    #     message['to'] = receiver
    #     message['subject'] = subject
    #     # 登录smtp服务器并发送邮件
    #     smtp = smtplib.SMTP()
    #     smtp.connect(smtpserver)
    #     smtp.login(username, passwd)
    #     smtp.sendmail(username, receiver, message.as_string())
    #     print("发送邮件{}成功".format(receiver))
    #     smtp.quit()
    #    except:
    #        print("发送失败")
    def send_emails(self, paths,emailconfig=True):
        try:
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
            # 创建压缩包附件
            if  emailconfig==True:
                with open(paths, 'rb') as file:
                    fujian = MIMEApplication(file.read())
                    fujian.add_header('Content-Disposition', 'attachment', filename=os.path.basename(paths))
                    message.attach(fujian)

                message['from'] = username
                message['to'] = receiver
                message['subject'] = subject

                # 登录smtp服务器并发送邮件
                smtp = smtplib.SMTP()
                smtp.connect(smtpserver)
                smtp.login(username, passwd)
                smtp.sendmail(username, receiver, message.as_string())
                print("发送邮件{}成功".format(receiver))
                smtp.quit()
            else:
                pass
        except:
            print("发送失败")
    def create_zip_file(self, images_path, zip_path, zip_name):
        """
        images_path = 'report/images'
        zip_path = 'archive'
        zip_name = 'archive.zip'
        :param images_path:
        :param zip_path:
        :param zip_name:
        :return:
        """
        current_dir = os.getcwd()
        images_abs_path = os.path.join(current_dir, images_path)
        zip_file_path = os.path.join(zip_path, zip_name)
        print(zip_file_path)
        with zipfile.ZipFile(zip_file_path, 'w') as zip_file:
            # 添加HTML文件到压缩包
            zip_file.write(self.get_latest_html_file(), os.path.basename(self.get_latest_html_file()))
            # 添加指定文件夹中的所有文件到压缩包
            for root, dirs, files in os.walk(images_abs_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    zip_file.write(file_path, os.path.join('images', os.path.relpath(file_path, images_abs_path)))


