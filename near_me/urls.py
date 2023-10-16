from django.urls import path
from near_me import views

app_name = "near_me"

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('receive_location/', views.receive_location, name='receive_location'),
]