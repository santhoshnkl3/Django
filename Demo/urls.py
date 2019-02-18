from django.urls import path

from django.conf.urls import url

from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('login/',views.index,name='login'),
    path('register/',views.register,name="register")
]
