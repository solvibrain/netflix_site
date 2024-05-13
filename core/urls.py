from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add-to-list',views.add_to_list,name="add-to-list"),
    path('login',views.user_login,name="user_login"),
    path("signup",views.user_signup, name="user_signup"),
    path("logout", views.user_logout, name="user_logout")


]