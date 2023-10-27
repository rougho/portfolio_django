from django.urls import path, include
from users.views import dashboard
from users.views import login_view

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("dashboard/", dashboard, name="dashboard"),
    path('login/', login_view, name="login")
]