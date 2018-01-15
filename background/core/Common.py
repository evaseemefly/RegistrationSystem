
import logging

class My_Log:
    pool=dict()

    def __new__(cls, log_type):
        obj=cls.pool.get(log_type,None)
        if not obj:
            obj=object.__new__(cls)
            cls.pool[log_type]=obj
            obj.log_type=log_type
        return obj

    def __init__(self,logpath='/log/log.tx'):
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        logfile = logpath
        filelog = logging.FileHandler(logfile, mode='w')
        filelog.setLevel(logging.DEBUG)

        consolelog = logging.StreamHandler()
        consolelog.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

        filelog.setFormatter(formatter)
        consolelog.setFormatter(formatter)

        logger.addHandler(filelog)
        logger.addHandler(consolelog)

    def getLogger(self):
        return logger
def log_init():
    # logging.basicConfig(level=logging.DEBUG,
    #                     filename='./log/log.tx',
    #                     filemode='w',
    #                     format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')





