from unicodedata import name
from django.urls import path
from manage import main
from . import views

urlpatterns = [
    path('signup',views.signuppage,name='signup'),
    path('login',views.loginpage,name='login'),
    path('logout',views.logoutpage,name='logout'),
] 