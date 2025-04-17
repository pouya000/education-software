from django.urls import path, include
from . import views

urlpatterns = [
    path('register', views.register,name="register_page"),
    path('login', views.loginFunction,name="login_page"),
    path('logout', views.logoutFunction, name="logout_page"),
    path('activation_account/<activation_code>', views.activeAccount, name="activation_account"),
]
