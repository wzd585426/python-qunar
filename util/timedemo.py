# -*- coding: utf-8 -*-
# @Time    : 2018/12/24 15:14
# @Author  : zhangyingying
# @Site    : 
# @File    : timedemo.py
# @Software: PyCharm
from datetime import datetime,timedelta

time=datetime.now()+timedelta(days=7)
time_date=time.strftime("%Y-%m-%d")
print(time_date)