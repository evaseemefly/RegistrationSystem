import os
from core import FileInfo
from conf import  settings
from datetime import datetime
from pandas import Series,DataFrame
import numpy as np
import pandas as pd
from conf import settings

def main():
    temp_date=datetime(2018,1,1)
    result_targetPath = os.path.join(settings.TARGET_DIR_PATH,
                              "%s%s.csv" % (temp_date.year, temp_date.month))
    ftpdir=settings.settings.FtpSourcePath
    savedir=settings.setting.TARGET_DIR_PATH
    excel_operate =FileInfo.ExcelOper(ftpdir,savedir)
    result= excel_operate.build()
    result.to_csv(result_targetPath)
    # excel_oper= FileInfo.ExcelOper()
    # derpartements=excel_oper.derpartments
    # length=excel_oper.getLen()
    # pass



if __name__=='__main__':
    main()