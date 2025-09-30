# chat/urls.py

from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('send-request/<int:user_id>/', views.send_friend_request, name='send_friend_request'),
    path('manage-request/<int:friendship_id>/<str:action>/', views.manage_friend_request, name='manage_friend_request'),
    path('chat/<str:username>/', views.private_chat_view, name='private_chat'),
]