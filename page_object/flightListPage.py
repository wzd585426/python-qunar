# -*- coding: utf-8 -*-
# @Time    : 2018/12/24 16:22
# @Author  : zhangyingying
# @Site    : 
# @File    : FlightListPage.py
# @Software: PyCharm

class FlightListPage:
    """
       机票搜索列表页面
       """
    current_url=""

    def __init__(self, driver):
        self.driver = driver
        self.current_url=driver.current_url

    def get_current_url(self):
        return self.current_url