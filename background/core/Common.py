
import logging

# LogType_dict={"info":logging.INFO,"debug":logging.DEBUG,"warning",logging.WARNING,"error":logging.ERROR,"critical":logging.CRITICAL}

LogType_dict={"info":logging.INFO,"debug":logging.DEBUG,"warning":logging.WARNING,"error":logging.ERROR,"critical":logging.CRITICAL}

class My_Log:
    """
    使用单例的方式，创建level唯一的logging
    注意由于logging本身，若通过Logging.getLogger(logname)的方式获取logger的话，多次调用听命的logger话只会返回相同的logger对象
    所以此处可以不使用单例模式，因为本身就是单例的（自己的理解）
    由于配置不是对当前的logger对象的，所以可以暂时先使用单例模式（我的尝试）
    """
    pool=dict()

    # def __new__(cls, log_type):
    #     obj=cls.pool.get(log_type,None)
    #     if not obj:
    #         obj=object.__new__(cls)
    #         cls.pool[log_type]=obj
    #         obj.log_type=log_type
    #     return obj

    def __new__(cls, log_type,logpath):
        obj=cls.pool.get(log_type,None)
        if not obj:
            # obj=object.__new__(cls)
            # cls.pool[log_type]=obj
            # obj.log_type=log_type
            '''
            根据log类型创建            
            '''
            # 1 创建logger对象
            logger = logging.getLogger()
            # logger.setLevel(LogType_dict(log_type))
            logger.setLevel(log_type)
            # 2 创建handler，用于写入日志文件
            logfile = logpath
            '''
            注意不会主动创建文件夹
                mode分为w 和 a
                w：对于已经存在的日志文件会覆盖，重写；
                a：对于已经存在的日志文件 会追加
            '''

            filelog = logging.FileHandler(logfile, mode='a')
            filelog.setLevel(log_type)
            # 3 创建控制台的handler
            consolelog = logging.StreamHandler()
            consolelog.setLevel(log_type)
            # 4 输出的内容
            formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

            filelog.setFormatter(formatter)
            consolelog.setFormatter(formatter)

            # 5 将logger添加至handler中
            logger.addHandler(filelog)
            logger.addHandler(consolelog)

            # obj=object.__new__(cls)
            cls.pool[log_type]=logger
            # obj.log_type=log_type
        return logger

    # def __init__(self,level=logging.DEBUG,logpath='/log/log.tx'):
    #     # 1 创建logger对象
    #     logger = logging.getLogger()
    #     logger.setLevel(logging.INFO)
    #     # 2 创建handler，用于写入日志文件
    #     logfile = logpath
    #     filelog = logging.FileHandler(logfile, mode='w')
    #     filelog.setLevel(logging.DEBUG)
    #     # 3 创建控制台的handler
    #     consolelog = logging.StreamHandler()
    #     consolelog.setLevel(logging.DEBUG)
    #     # 4 输出的内容
    #     formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
    #
    #     filelog.setFormatter(formatter)
    #     consolelog.setFormatter(formatter)
    #
    #     # 5 将logger添加至handler中
    #     logger.addHandler(filelog)
    #     logger.addHandler(consolelog)

    def getLogger(self,log_type):
        return self.pool.get(log_type)

        # return True
# def log_init():
    # logging.basicConfig(level=logging.DEBUG,
    #                     filename='./log/log.tx',
    #                     filemode='w',
    #                     format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

# my_log=My_Log(logging.INFO,'../log/log.txt')
# # my_log=my_log.getLogger(logging.INFO)
# my_log.info("测试123123")
# pass

