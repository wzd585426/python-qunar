# -*- coding: utf-8 -*-
# @Time    : 2018/12/26 10:07
# @Author  : zhangyingying
# @Site    : 
# @File    : run.py
# @Software: PyCharm
import unittest
from unittest import TextTestRunner

from util.createReport import run_and_createReport
from util.sendEmail import send_email, send_email_attach

if __name__ == '__main__':
    suite = unittest.defaultTestLoader.discover("./testcase", pattern="*Test.py")
    # TextTestRunner().run(suite)
    file_name=run_and_createReport(suite)
    send_email_attach(file_name)

