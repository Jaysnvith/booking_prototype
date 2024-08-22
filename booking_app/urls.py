from django.urls import path
from . import views

app_name='booking_app'
urlpatterns = [
    path('', views.BookingHome, name="home"),
    
    path('room-<int:pk>/', views.RoomDetail, name='room'),
    path('room-<int:pk>/update/', views.RoomUpdate.as_view(), name='room_update'),
    path('room-<int:pk>/delete/', views.RoomDelete.as_view(), name='room_delete'),
    
    path('booking-<int:pk>/', views.BookingDetail.as_view(), name='booking'),
    path('booking/new/', views.BookingNew.as_view(), name='booking_new'),
    path('booking-<int:pk>/update/', views.BookingUpdate.as_view(), name='booking_update'),
    path('booking-<int:pk>/delete/', views.BookingDelete.as_view(), name='booking_delete'),
]