# -*- coding: utf-8 -*-
# @Time    : 2018/12/26 10:05
# @Author  : zhangyingying
# @Site    : 
# @File    : createReport.py
# @Software: PyCharm
import os
import time
from HTMLTestRunner import HTMLTestRunner


def run_and_createReport(suite):
    time_stamp=time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime())
    base_path=os.path.dirname(__file__)
    fn=base_path.replace("util","report/Qunar测试报告"+time_stamp+".html")
    # file_path=open(fn,"wb")

    with open(fn,"wb") as file_path:
        runner = HTMLTestRunner(stream=file_path, verbosity=1, title="测试报告", description="Qunar机票搜索")
        runner.run(suite)
    # file_path.close()
    return fn

