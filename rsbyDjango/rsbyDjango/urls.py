"""rsbyDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
# from django.urls import reverse
from django.contrib import admin
# from django.utils.functional import lazy
# from django.utils.functional import lazy_property
import xadmin
xadmin.autodiscover()

from rsdb import views
import rsdb
from duty import views
# import duty

from rest_framework.authtoken import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^xadmin/', xadmin.site.urls,name='xadmin'),
    url(r'^home',rsdb.views.home),
    # url(r'^getPersonList',views.getPersonList),
    url('^duty/',include('duty.urls',namespace='duty')),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^api-token-auth/', views.obtain_auth_token)
]

