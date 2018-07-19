
from django.conf.urls import url
from . import views
app_name="users"

urlpatterns=[
    url(r'^auth/$',views.UserListView.as_view()),
    url(r'^detail/$',views.AuthorDetialView.as_view()),
    url(r'^authdepdutylist/$',views.AuthDepartmentDutyView.as_view())
]