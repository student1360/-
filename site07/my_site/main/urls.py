from django.urls import path
from . import views
from .views import register_view, login_view, logout_view

urlpatterns = [
    path('', views.index),
    path('page/', views.page),
    path('page1/', views.page1),
    path('page2/', views.page2),
    path('page3/', views.page3),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]