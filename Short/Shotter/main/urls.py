from django.contrib import admin
from django.urls import path
from .views import index, NewPerson, NewPersonLogin, NewPersonLogout, checkurl, allurls


urlpatterns = [
    path('', index, name='index'),
    path('signup/', NewPerson.as_view(), name='signup'),
    path('login/', NewPersonLogin.as_view(), name='login'),
    path('logout/', NewPersonLogout.as_view(), name='logout'),
    path('checkurl/', checkurl, name='checkurl'),
    path('allurls', allurls, name='allurls'),
]