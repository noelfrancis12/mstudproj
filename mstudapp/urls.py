from django.contrib import admin
from django.urls import path,include
from.import views
urlpatterns = [
    path('',views.home,name='home'),
    path('usercreate',views.usercreate,name='usercreate'),
    path('loginpage',views.loginpage,name='loginpage'),
    path('login1',views.login1,name='login1'),
    path('logout',views.logout,name='logout'),
    path('signup',views.signup,name='signup'),
    path('about',views.about,name='about'),
    path('addc',views.addc,name='addc'),
    path('adds',views.adds,name='adds'),
    path('show',views.show,name='show'),
]