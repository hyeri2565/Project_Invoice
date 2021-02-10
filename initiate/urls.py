from django.conf.urls import url
from . import views
from django.urls import path

app_name='initiate'
urlpatterns=[
    path('',views.index,name='index'),
    path('login/',views.loginTest,name='testlogin'),
    path('auth/',views.login_view,name='auth'),
    path('logout/',views.logout_view,name='outauth')
]