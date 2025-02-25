from django.urls import path
from . import views
from .views import register_view, login_view, logout_view

urlpatterns = [
    path('', views.index),
    path('page/', views.page),
    path('page1/', views.page1),
    path('page2/', views.page2),
    path('page3/', views.page3),
    path('page4/', views.page4),
    path('page5/', views.page5),
    path('page6/', views.page6),
    path('page7/', views.page7),
    path('page8/', views.page8),
    path('test/', views.test),
    path('profile/', views.profile),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
