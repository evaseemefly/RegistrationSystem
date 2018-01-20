import os

BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ftp上传的根目录
# 单位电脑
# FtpSourcePath=r"E:\03协同开发\九楼值班显示平台\ftpdir"
# TARGET_DIR_PATH=r"E:\03协同开发\九楼值班显示平台\result"

#surface book
# FtpSourcePath=r"D:\git仓库\RegistrationSystem\background\ftpdir"
# TARGET_DIR_PATH=r"D:\git仓库\RegistrationSystem\background\result"
FtpSourcePath=r"/Users/liusihan/Documents/GitHub/RegistrationSystem/background/ftpdir"
TARGET_DIR_PATH=r"/Users/liusihan/Documents/GitHub/RegistrationSystem/background/result"


#最终输出的文件的前缀
RESULT_FILE_NAME='MERAGE_'
RESULT_FILE_EXT='.pk1'

LOG_DIR=r'../log'

REDIS_IP='127.0.0.1'
REDIS_PORT=6379
#redis过期时间
REDIS_EX=85400

NAME_DaySavedInRedis='dailydata'