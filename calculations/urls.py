from django.urls import path
from . import views

urlpatterns = [
    path('', views.room_list, name='room_list'),
    path('room/<int:pk>/', views.room_detail, name='room_detail'),
    path('room/new/', views.room_new, name='room_new'),
    path('buildings/', views.building_list, name='building_list'),
    path('building/<int:pk>/', views.building_detail, name='building_detail'),
    path('building/new/', views.building_new, name='building_new'),
]
