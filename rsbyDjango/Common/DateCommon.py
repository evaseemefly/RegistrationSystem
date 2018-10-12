from datetime import datetime,date,timedelta
import calendar


def getMonthDateRang(target_date):
    '''
        获取指定日期的该月的全部日期
    :param target_date:
    :return:
    '''
    # 获取指定月份的全部日期
    start_date=target_date.replace(day=1)
    _,days_in_month=calendar.monthrange(target_date.year,target_date.month)
    end_date=start_date+timedelta(days=days_in_month)

    return (start_date,end_date)

def getMonthDateList(target_date):
    '''
        根据传入的日期获取该月份的全部时间列表
    :param target_date:
    :return:
    '''
    date_list=[]
    first_day,last_day= getMonthDateRang(target_date)
    a_day=timedelta(days=1)
    while first_day<last_day:
        date_list.append(first_day)
        first_day+=a_day

    return date_list