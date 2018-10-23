
from django.conf.urls import url

from . import views

app_name = 'duty'
urlpatterns = [
    url(r'^list/$', views.DutyListView.as_view(), name='list'),
    url(r'^schedulelist/$',views.ScheduleListView.as_view(),name='schedulelist'),
    url(r'^userlist/',views.UserListView.as_view(),name='userlist'),
    url(r'^dutylist/',views.DutyListView.as_view(),name="dutylist"),
    url(r'^modity/',views.ScheduleModificationView.as_view()),
    url(r'^grouplist/',views.GroupListView.as_view()),
    url(r'^schedulelist/creat/$',views.ScheduleCreateView.as_view()),
    url(r'^schedulelist/del/$',views.ScheduleDelView.as_view()),
    url(r'^create/user$',views.CreateUserView.as_view()),
    url(r'^demo/$',views.DutyDemoView.as_view()),
    url(r'^schdeulelistshow/$',views.ScheduleShowListView.as_view()),

    url(r'^schdeulestaticlistshow/$',views.ScheduleShowStaticListView.as_view()),
    url(r'^departmentlist/$',views.DepartmentListView.as_view()),
    # 根据部门did获取该部门的部门联系list
    url(r'^departmentcontactlist/$',views.DepartmentConactListView.as_view()),
    # 根据输入的起止时间和department的did信息，统计时间范围内指定department值班总数
    url(r'^departmentStatistics/',views.DepartmentStatisticsView.as_view()),
    # 根据时间，部门id获取该月份的岗位及人数
    url(r'^departmentScheduleStatistics/',views.DutyUserStatisticsView.as_view())
]