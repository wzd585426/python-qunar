# -*- coding: utf-8 -*-
# @Time    : 2018/12/24 15:39
# @Author  : zhangyingying
# @Site    : 
# @File    : flightpage.py
# @Software: PyCharm
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from page_object.flightListPage import FlightListPage


class FlightSearchPage:
    """
    机票搜索页面
    """
    url="http://flight.qunar.com"
    loc_from_city_input=(By.NAME,"fromCity")
    loc_to_city_input=(By.XPATH,'//*[@id="dfsForm"]/div[2]/div[2]/div/input')
    loc_from_date=(By.ID,"fromDate")
    loc_search_btn=(By.CLASS_NAME,"btn_search")

    def __init__(self,driver):
        self.driver=driver

    def open_page(self):
        self.driver.get(self.url)

    def input_from_city(self,from_city):
        self.driver.find_element(*self.loc_from_city_input).click()
        self.driver.find_element_by_link_text(from_city).click()
        time.sleep(3)
        ActionChains(self.driver).send_keys(Keys.TAB).perform()

    def input_to_city(self,to_city):
        self.driver.find_element(*self.loc_to_city_input).click()
        self.driver.find_element_by_link_text(to_city).click()

    def input_from_date(self,from_date):
        self.driver.find_element(*self.loc_from_date).send_keys(from_date)

    def click_search_btn(self):
        self.driver.find_element(*self.loc_search_btn).click()
        return FlightListPage(self.driver)


