
from django.conf.urls import url

from . import views

app_name = 'duty'
urlpatterns = [
    url(r'^list/$', views.DutyListView.as_view(), name='list'),
    url(r'^schedulelist/$',views.ScheduleListView.as_view(),name='schedulelist'),
    url(r'^userlist/',views.UserListView.as_view(),name='userlist'),
    url(r'^dutylist/',views.DutyListView.as_view(),name="dutylist"),
    url(r'^modity/',views.ScheduleModificationView.as_view())
]