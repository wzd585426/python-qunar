# -*- coding: utf-8 -*-
# @Time    : 2018/12/26 16:33
# @Author  : zhangyingying
# @Site    : 
# @File    : createImage.py
# @Software: PyCharm
import os
import time


def create_png(driver,case_name):
    time_stamp = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
    base_path = os.path.dirname(__file__)
    fn = base_path.replace("util", "image/"+case_name+"_"+ time_stamp + ".png")
    driver.get_screenshot_as_file(fn)