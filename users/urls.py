from django.urls import path
from .views import signup,loginn,home,logoutt
urlpatterns=[
    path('signup/',signup,name='signup'),
    path('login/',loginn,name='login'),
    path('home/',home,name='home'),
    path('logout/',logoutt,name='logout')
]