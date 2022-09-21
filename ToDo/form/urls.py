from django.urls import path
from . import views

app_name= "form"

urlpatterns = [
    path("", views.login_user, name="loginUser"),
    path("register/", views.register_user, name="registerUser"),
    path("main/", views.mainf , name="main")
]