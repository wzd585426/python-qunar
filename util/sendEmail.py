# -*- coding: utf-8 -*-
# @Time    : 2018/12/26 10:06
# @Author  : zhangyingying
# @Site    : 
# @File    : sendEmail.py
# @Software: PyCharm
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP, SMTP_SSL

# 邮件设置信息
from util.readFile import read_csv



email_info={
    "host":"smtp.126.com",
    "port":465,
    "username":"zyy2019@126.com",
    "password":"zyy2018",
    "mailType":"html",
    "fromAddr": "zyy2019@126.com",
    "toAddrs": "",
    "mailSubject":"Qunar机票搜索测试报告",
    "mailEncoding":"utf-8"
}


def send_email_attach(file_name):
    to_addrs = getAllReciver()

    # 读取要发送的邮件内容

    file = open(file_name, 'rb')
    file_content = file.read()
    file.close()

    # 带附件的实例
    mime =MIMEMultipart()
    mime["Subject"] = email_info["mailSubject"]
    mime["From"] = email_info["fromAddr"]
    mime["To"] = ",".join(to_addrs)

    # 邮件正文
    mime.attach(MIMEText(file_content, _subtype=email_info["mailType"], _charset=email_info["mailEncoding"]))

    # 附件1
    html_attachment = MIMEText(open(file_name, 'rb').read(), 'base64', 'utf-8')
    html_attachment["Content-Type"] = 'application/octet-stream'
    html_attachment["Content-Disposition"] = 'attachment; filename="test_port.html"'
    mime.attach(html_attachment)
    # 附件2
    img_attachment = MIMEText(open(file_name, 'rb').read(), 'base64', 'utf-8')

    # imageFile = '1.png'
    # imageApart = MIMEImage(open(imageFile, 'rb').read(), imageFile.split('.')[-1])
    # imageApart.add_header('Content-Disposition', 'attachment', filename=imageFile)
    smtp= SMTP_SSL(email_info["host"],email_info["port"])
    smtp.login(email_info["username"], email_info["password"])
    smtp.sendmail(email_info["fromAddr"], to_addrs, mime.as_string())
    smtp.close()

    print("邮件发送成功！")


def send_email(file_name):
    print("邮件设置参数")

    # 收件人
    to_addrs = getAllReciver()

    # 读取要发送的邮件内容
    file = open(file_name, 'rb')
    file_content=file.read()
    file.close()
    # 设置邮件内容为MIME格式
    mime = MIMEText(file_content, _subtype=email_info["mailType"], _charset=email_info["mailEncoding"])
    mime["Subject"] = email_info["mailSubject"]
    mime["From"] = email_info["fromAddr"]
    mime["To"] = ",".join(to_addrs)
    print("邮件发送开始。。。")

    # 使用smtp协议发送邮件

    # SMTP()与SMTP_SSL()的区别：前者是明文传输，后者是先建立SSL安全连接再进行传输，也可加密密钥
    # smtp=SMTP(email_info["host"])
    smtp= SMTP_SSL(email_info["host"],email_info["port"])
    smtp.login(email_info["username"], email_info["password"])
    smtp.sendmail(email_info["fromAddr"], to_addrs, mime.as_string())
    smtp.close()

    print("邮件发送成功！")

def getAllReciver():
    all_recivers = read_csv("report_receivers.csv")
    to_addrs = []
    for addr in all_recivers:
        to_addrs.append(addr[1])
    return to_addrs

