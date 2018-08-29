
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
    url(r'^tempTestJson/$',views.tempTestJson),
	url(r'^scheduleshowlist/',views.ScheduleShowListView.as_view())
]