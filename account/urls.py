from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('login', views.loginFr, name="log_in"),
    path('signup', views.signFr, name="sign_up"),
    path('logout', views.logOut, name="logout")
]