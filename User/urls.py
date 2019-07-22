# encoding:utf-8

from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = '[User]'

urlpatterns = [
    path('', views.index),
    path('index/', views.index),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('sign_out/', views.sign_out, name='sign_out'),

]

# 设置静态文件路径
urlpatterns += staticfiles_urlpatterns()
