# -*- coding:utf-8 -*-

import xlrd

import os
from pandas import Series,DataFrame
import numpy as np
import pandas as pd
import datetime

# file_name='data/201712.xlsx'
file_name='data/convert_1.xlsx'

data=xlrd.open_workbook(file_name)

table=data.sheets()[0]



# f=open('data/201712.xlsx')
# '''
#     此处出错：UnicodeDecodeError: 'gbk' codec can't decode byte 0xee in position 99: illegal multibyte sequence
# '''
# read_data=pd.read_csv(f,sep='\s',encoding='UTF-8')


# 使用pandas读取excel
read_data=pd.read_excel(file_name,sheetname=0)
pass