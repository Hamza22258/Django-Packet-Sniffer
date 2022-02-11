from django.contrib import admin
from django.urls import path
from .views import PacketView, Main, Stop, Delete

urlpatterns = [
    path('getPackets/', PacketView.as_view()),
    path('start/', Main.Start.as_view()),
    path('stop/', Main.Start.as_view()),
    path('delete/', Delete.as_view()),
]
