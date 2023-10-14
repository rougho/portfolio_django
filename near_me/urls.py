from django.urls import path
from near_me import views

app_name = "near_me"

urlpatterns = [
    path('', views.home)
]