# -*- coding: utf-8 -*-
# @Time    : 2018/12/24 15:57
# @Author  : zhangyingying
# @Site    : 
# @File    : filghtSearchTest.py
# @Software: PyCharm
from basecase.baseTestCase import BaseTestCase
from page_object.flightpage import FlightSearchPage
from util.createImage import create_png


class FlightSearchTest(BaseTestCase):


    def test_search(self):

        searchPo=FlightSearchPage(self.driver)
        searchPo.open_page()
        searchPo.input_from_city("北京")
        searchPo.input_to_city("上海")
        searchPo.input_from_date("2019-01-01")
        listPo=searchPo.click_search_btn()


        create_png(self.driver,"test_search")
        self.assertIn("oneway_list.htm?searchDepartureAirport=",listPo.get_current_url())

