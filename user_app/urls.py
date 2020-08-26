from django.urls import path
from . import views

urlpatterns = [
        path('online-users', views.OnlineUserListView.as_view(), name='online-users'),
]
