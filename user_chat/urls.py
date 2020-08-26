from django.urls import path
from . import views

urlpatterns = [
        path('create-chat-room', views.ChatRoomView.as_view(), name='initiate-chat'),
]
