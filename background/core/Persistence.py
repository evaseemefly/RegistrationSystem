from pandas import Series,DataFrame
import numpy as np
import pandas as pd
from abc import ABCMeta, abstractmethod
import pickle

class Base_Persistence(object):
    '''
    供子类继承，并实现to_persistence抽象方法的父类
    '''
    def __init__(self,df,path):
        '''

        :param df: 传入的dataframe
        :param path: 保存路径（最终文件全名称）
        '''
        self.df = df
        self.path = path

    @abstractmethod
    def to_persistence(self):
        pass

    @abstractmethod
    def read_persistence(self,readpath):
        pass

class Excel_Persistence(Base_Persistence):
    '''
    excel的持久化保存实现类
    '''
    def __init__(self,df,path):
        '''
        :param df:传入的dataframe
        :param path:保存到的路径
        '''
        super(Excel_Persistence, self).__init__(df,path)

        pass

    def to_persistence(self):
        '''
        持久化（本地保存）
        :return:
        '''
        if self.df is not None:
            self.df.to_csv(self.path)
        pass

    def read_persistence(self, readpath):
        pass

class Pickle_Persistence(Base_Persistence):
    '''
    使用Pickle的持久化保存实现类
    '''
    def __init__(self,df,path):
        super(Pickle_Persistence, self).__init__(df,path)
        pass

    def to_persistence(self):
        '''
        使用pickle实现持久化保存需要
        :return:
        '''
        self.df.to_pickle(self.path)

    def read_persistence(self, readpath):
        return pd.read_pickle(readpath)



class Persistence_Environment(object):
    '''
    从此开始使用新式类
    '''

    def __init__(self,factory):
        self.persistence_instance = factory

    def make_persistence(self):
        self.persistence_instance.to_persistence()
        # self.persistence_instance=factory

    def read_persistence(self,readpath):
        self.persistence_instance.read_persistence(readpath)

    # def run(self):
    #     self.persistence_instance.to_persistence()