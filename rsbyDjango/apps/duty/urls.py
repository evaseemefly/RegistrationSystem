
from django.conf.urls import url

from . import views

app_name = 'duty'
urlpatterns = [
    url(r'^list/$', views.DutyListView.as_view(), name='list'),
    # 获取值班信息
    url(r'^schedulelist/$',views.ScheduleListView.as_view(),name='schedulelist'),
    url(r'^userlist/',views.UserListView.as_view(),name='userlist'),
    url(r'^dutylist/',views.DutyListView.as_view(),name="dutylist"),
    url(r'^modity/',views.ScheduleModificationView.as_view()),
    url(r'^grouplist/',views.GroupListView.as_view()),
    # 创建值班信息
    url(r'^schedulelist/creat/$',views.ScheduleCreateView.as_view()),
    url(r'^schedulelist/del/$',views.ScheduleDelView.as_view()),
    url(r'^create/user$',views.CreateUserView.as_view()),
    url(r'^demo/$',views.DutyDemoView.as_view()),
    url(r'^schdeulelistshow/$',views.ScheduleShowListView.as_view()),
    # 左侧固定位置的两人
    url(r'^schdeulestaticlistshow/$',views.ScheduleShowStaticListView.as_view()),
    url(r'^departmentlist/$',views.DepartmentListView.as_view())
]