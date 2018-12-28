# -*- coding: utf-8 -*-
# @Time    : 2018/12/28 11:27
# @Author  : zhangyingying
# @Site    : 
# @File    : readCsvFile.py
# @Software: PyCharm
import csv
import os


def read_csv(file_name):
    data_list=[]
    base_path=os.path.dirname(__file__)
    file_path=base_path.replace("util","data/"+file_name)
    with open(file_path) as file:
        content = csv.reader(file)
        i=0
        for row in content:
            if i==0:
                pass
            else:
                data_list.append(row)
            i=i+1

    return data_list


def read_xls():
    pass

def read_xlsx():
    pass


if __name__ == '__main__':
    data_list=read_csv("report_receivers.csv")
    print(data_list)