# -*- coding:utf-8 -*-

import xlrd

import os
from pandas import Series,DataFrame
import numpy as np
import pandas as pd
import datetime

# file_name='data/201712.xlsx'
# file_name='data/convert_1.xlsx'
#
# data=xlrd.open_workbook(file_name)
#
# table=data.sheets()[0]



# f=open('data/201712.xlsx')
# '''
#     此处出错：UnicodeDecodeError: 'gbk' codec can't decode byte 0xee in position 99: illegal multibyte sequence
# '''
# read_data=pd.read_csv(f,sep='\s',encoding='UTF-8')


# 使用pandas读取excel
file_name='data/convert_3.xlsx'
read_data=pd.read_excel(file_name,sheetname=0,header=None)

columns_names=read_data.iloc[0:2,1:]
columns_names.columns=np.arange(columns_names.shape[1])

def dumpingNan(df):
    def replaceNan(df, index_colunms, index_rows):
        '''
        index_colunms:列
        inde_rows:行
        '''
        # 此处可能存在的问题是由于是or 所以是否需要两个条件都需要进行判断，若第一个判断为true的话第二个条件进行判断时会出错
        # if index_colunms >= df.shape[1] - 1 or df[index_colunms + 1][index_row] is np.nan:
        if index_colunms >= df.shape[1] - 1:

            # 若右侧补齐超出边界，或右侧值为null，则进行左侧补齐
            # if index_colunms <= 0 or df[index_colunms - 1][index_rows] is np.nan:
            # 不能向左找了，只能向右侧找
            if index_colunms <= 0:
                # 位置左移
                index_colunms += 1
                # 递归
                df = replaceNan(df, index_colunms, index_rows)
            else:
                if df[index_colunms - 1][index_rows] is np.nan:
                    df[index_colunms][index_rows] = df[index_colunms - 1][index_rows]
        else:
            df[index_colunms][index_rows] = df[index_colunms + 1][index_rows]
        return df

    # 找到isnull的位置
    index_null = np.where(df.isnull())
    index_array = np.array(index_null).T
    #     print(columns_names.shape[1])
    # 遍历二维数组
    count = len(index_array)
    for temp in index_array:
        # 行号
        index_row = temp[0]
        # 列号
        index_columns = temp[1]

        '''
            注意与df的索引方式正好相反
            df是先列，再行
        '''
        df = replaceNan(df, index_columns, index_row)


result = dumpingNan(columns_names)
pass