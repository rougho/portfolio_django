from django.urls import path
from users.views import dashboard
from users.views import log_in

urlpatterns = [
    path("dashboard/", dashboard, name="dashboard"),
    path('log_in/', log_in, name="log_in")
]