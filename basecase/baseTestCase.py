# -*- coding: utf-8 -*-
# @Time    : 2018/12/24 15:40
# @Author  : zhangyingying
# @Site    : 
# @File    : baseTestCase.py
# @Software: PyCharm
import time
import unittest

from selenium import webdriver


class BaseTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
